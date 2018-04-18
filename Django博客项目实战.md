# django 1.10.6 项目实战

### 安装Django实战必备环境

强烈推荐在 Virtualenv 下进行 Django 的开发。**Virtualenv 是一个 Python 工具，使用它可以创建一个独立的 Python 环境。

为什么要使用 Virtualenv 呢？举个例子，假设你已经在系统中安装了 Python，并且在阅读此教程前你已经进行过一些 Django 的学习，但那时候安装的 Django 还是 1.8 版本。我们教程使用的是最新版的 Django 1.10.6 版本，你可能不愿意删除掉旧版的 Django 1.8，因为那可能导致你以前的项目无法运行。既想让原本项目在 Django 1.8 环境下运行，又想再安装 Django 1.10.6 来开启本教程的项目，怎么办呢？使用 Virtualenv 就能够完美解决这个问题。

Virtualenv 帮我们从系统的 Python 环境中克隆一个全新的 Python 环境出来，这个环境独立于原来的 Python 环境。我们可以在这个新克隆的环境下安装 Django 1.10.6，并且在这个新环境下运行我们的新项目。

Virtualenv 的使用非常简单，首先安装 Virtualenv，打开命令行工具，输入 `pip install virtualenv` 命令即可安装 Virtualenv。

```python
pip install virtualenv
Collecting virtualenv
  Downloading virtualenv-15.2.0-py2.py3-none-any.whl (2.6MB)
    100% |████████████████████████████████| 2.6MB 22kB/s 
Installing collected packages: virtualenv
Successfully installed virtualenv-15.2.0
```

看到上面这样的内容就代表你的virtualenv包安装成功了。



安装成功后  开始创建虚拟环境，制定一个你喜欢的目录，任何地方都可以，执行一下命令

```python
virtualenv venvProject # 这里你可以制定任何位置和目录，我这里是在当前目录下创建的
# 一下是命令行运行结果
New python executable in /Users/bene/Desktop/djangoBlog_env/venvProject/bin/python
Installing setuptools, pip, wheel...done.
# 看到这说明已经成功了
```

然后执行命令激活虚拟环境 `source venvProject/bin/activate`

```python
source venvProject/bin/activate
# 当你的命令行窗口显示如下信息表示已经切换到虚拟环境
(venvProject) benedeMacBook-Pro:djangoBlog_env bene$
```

走到这一步就必须要恭喜了  虚拟环境安装好了，接下来就是办正事，安装web开发必备的Django，在虚拟环境中执行命令`pip install django == 1.10.6`

```python
(venvProject) benedeMacBook-Pro:djangoBlog_env bene$ pip install django==1.10.6
Collecting django==1.10.6
  Downloading Django-1.10.6-py2.py3-none-any.whl (6.8MB)
    100% |████████████████████████████████| 6.8MB 198kB/s 
Installing collected packages: django
Successfully installed django-1.10.6
```

提示信息表示你已经安装成功了，我们在python解释器中调用一下看看结果：

```python
(venvProject) benedeMacBook-Pro:djangoBlog_env bene$ python
Python 3.6.3 |Anaconda, Inc.| (default, Oct  6 2017, 12:04:38) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
1.10.6
>>> 
```

perfect，我们已经成功安装了Django1.10.6版本，接下来就是进行工程创建了。



### 创建Django工程

万事俱备，让我们来创建Django工程吧！



首先进入一个你想进入的任何位置，在这里你打算把工程放在这个位置，Linux的文件管理命令我就不再此赘述了。

```python
django-admin startproject blogproject #在你想创建工程的位置执行这个命令，会自动给你创建一个blogproject的工程目录
```

然后执行tree命令看下工程结构

```python
benedeMacBook-Pro:blogproject bene$ tree
.
├── blogproject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
```

最顶层的 blogproject目录是我们刚刚指定的工程目录。blogproject 目录下面有一个 manage.py 文件，manage 是管理的意思，顾名思义 manage.py 就是 Django 为我们生成的管理这个项目的 Python 脚本文件，以后用到时会再次介绍。与 manage.py 同级的还有一个 blogproject\ 的目录，这里面存放了一些 Django 的配置文件，例如 settings.py、urls.py 等等，以后用到时会详细介绍。



### hello django

网站需要运行在一个 Web 服务器上，Django 已经为我们提供了一个用于本地开发的 Web 服务器。在命令行工具里进入到 manage.py 所在目录，即**最外层**的 blogproject\ 目录下。运行 `python manage.py runserver` 命令就可以在本机上开启一个 Web 服务器：

```python
(venvProject) benedeMacBook-Pro:blogproject bene$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

April 06, 2018 - 10:57:56
Django version 1.10.6, using settings 'blogproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

可以看到本地服务器已经启动，在网页中输入地址`http://127.0.0.1:8000/`会弹出一个界面，it works，表示已经成功啦！Django已经开始工作啦。Django 默认的语言是英语，所以显示给我们的欢迎页面是英文的。我们在 Django 的配置文件里稍作修改，让它支持中文。用任何一个文本编辑器打开 settings.py 文件，找到如下的两行代码：

```python
blogproject/blogproject/settings.py

## 其它配置代码...

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

## 其它配置代码...	
```

把 `LANGUAGE_CODE` 的值改为 `zh-hans`，`TIME_ZONE` 的值改为 `Asia/Shanghai`：

```python
blogproject/blogproject/settings.py

## 其它配置代码...

# 把英文改为中文
LANGUAGE_CODE = 'zh-hans'

# 把国际时区改为中国时区
TIME_ZONE = 'Asia/Shanghai'

## 其它配置代码...
```

**保存更改后**关闭 settings.py 文件。

再次运行开发服务器，并在浏览器打开 http://127.0.0.1:8000/，可以看到 Django 已经支持中文了。

![image-20180407101834492](/var/folders/l2/_2gdknxs0xv2frxr0kzdj79h0000gn/T/abnerworks.Typora/image-20180407101834492.png)

非常完美。



### 建立博客应用

Django为我们提供了自动创建应用的命令`python manage.py startapp blog`，在Django工程根目录，也就是和manage.py同级目录下执行此命令

```python
benedeMacBook-Pro:blogproject bene$ python manage.py startapp blog
benedeMacBook-Pro:blogproject bene$ tree
.
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── blogproject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py

4 directories, 17 files
```

我们可以看到在这个blogproject目录下又多了一个blog目录，这个就是我们的应用目录。不同的文件代表不同的功能，我们创建了一个Django应用，我们还必须要告诉Django，注册这个应用，来到settings.py配置文件，进行应用注册

```python
blogproject/blogproject/settings.py

## 其他配置项...

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog', # 注册 blog 应用
]

## 其他配置项...
```

