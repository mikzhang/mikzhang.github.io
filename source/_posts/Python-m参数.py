---
title: Python-m参数
date: 2017-09-28 14:30:38
categories: Python
tags:
    - Python
---

python xxx.py和python -m xxx.py有什么区别?

<!-- more -->

## -m 作用
python -m xxx.py 作用是把 xxx.py 文件当做模块启动
man python 查看 python 文档
```
-m module-name
    Searches sys.path for the named module and runs the corresponding .py file as a script.
```

## 区别

1. python xxx.py
2. python -m xxx.py

这是两种加载py文件的方式:
1叫做直接运行
2把模块当作脚本来启动(注意：但是__name__的值为'main' )

**不同的加载py文件的方式，主要是影响——sys.path 这个属性。sys.path 就相当于liunx中的PATH。**

下面来看一下sys.path
```python
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',  
...]
```
上面的内容我只截取了一段。此为当前python解释器运行的环境，python解释器会在这些目录下去寻找依赖的库!
注解一点：‘''——为当前目录

下面有两个例子，通过不同方式启动同一文件，sys.path属性的值有何不同。
run.py 内容如下:
```python
import sys
print(sys.path)
```

直接启动：python run.py
```python
test_import_project git:(master) ✗ python run.py
['/Users/sx/Documents/note/test_py/test_import_project',  
 '/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',  
  ...]
```

以模块方式启动：python -m run.py
```python
test_import_project git:(master) ✗ python -m run.py
['',  
 '/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
```
** 细心的同学会发现，区别就是在第一行。直接启动是把run.py文件，所在的目录放到了sys.path属性中。模块启动是把你输入命令的目录（也就是当前路径），放到了sys.path属性中**

## 应用场景

目录结构如下
```python
package/
    __init__.py
    mod1.py
package2/
    __init__.py
    run.py
```

run.py 内容如下
```python
import sys
from package import mod1
print(sys.path)
```
如何才能启动run.py文件？
```python
# 直接启动（失败）
➜  test_import_project git:(master) ✗ python package2/run.py
Traceback (most recent call last):
  File "package2/run.py", line 2, in <module>
    from package import mod1
ImportError: No module named package

# 以模块方式启动（成功）
➜  test_import_project git:(master) ✗ python -m package2.run
['',
'/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
...]
```
当需要启动的py文件引用了一个模块。你需要注意：在启动的时候需要考虑sys.path中有没有你import的模块的路径！
这个时候，到底是使用直接启动，还是以模块的启动？目的就是把import的那个模块的路径放到sys.path中。你是不是明白了呢？
```
官方文档参考： http://www.pythondoc.com/pythontutorial3/modules.html
```

## 总结
导入一个叫 mod1 的模块时，解释器先在当前目录中搜索名为 mod1.py 的文件。如果没有找到的话，接着会到 sys.path 变量中给出的目录列表中查找。 sys.path 变量的初始值来自如下：

输入脚本的目录（当前目录）。
环境变量 PYTHONPATH 表示的目录列表中搜索(这和 shell 变量 PATH 具有一样的语法，即一系列目录名的列表)。
Python 默认安装路径中搜索。
实际上，解释器由 sys.path 变量指定的路径目录搜索模块，该变量初始化时默认包含了输入脚本（或者当前目录）， PYTHONPATH 和安装目录。这样就允许 Python程序了解如何修改或替换模块搜索目录。

ref:[http://www.cnblogs.com/xueweihan/p/5118222.html?utm_source=tuicool&utm_medium=referral](http://www.cnblogs.com/xueweihan/p/5118222.html?utm_source=tuicool&utm_medium=referral)
