# DjangoBlog

🌍
*[English](/docs/README-en.md) ∙ [Simplified Chinese](README.md)*

A blog based on `python3.8` and `Django3.0`.

[![Django CI](https://github.com/liangliangyy/DjangoBlog/actions/workflows/django.yml/badge.svg)](https://github.com/liangliangyy/DjangoBlog/actions/workflows/django .yml) [![CodeQL](https://github.com/liangliangyy/DjangoBlog/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/liangliangyy/DjangoBlog/actions /workflows/codeql-analysis.yml) [![codecov](https://codecov.io/gh/liangliangyy/DjangoBlog/branch/master/graph/badge.svg)](https://codecov.io/gh /liangliangyy/DjangoBlog) [![Requirements Status](https://requires.io/github/liangliangyy/DjangoBlog/requirements.svg?branch=master)](https://requires.io/github/liangliangyy/DjangoBlog/ requirements/?branch=master) [![license](https://img.shields.io/github/license/liangliangyy/djangoblog.svg)]()

## Main functions:
-Add, delete, edit articles, pages, categories, tags, etc. Articles and pages support `Markdown`, and support code highlighting.
-Support full text search of articles.
-Complete comment function, including posting reply comments, and email reminders of comments, supporting `Markdown`.
-Sidebar function, latest articles, most read, tag cloud, etc.
-Support Oauth login, now there are Google, GitHub, facebook, Weibo, QQ logins.
-Support `Memcache` cache, support automatic cache refresh.
-Simple SEO function, new articles, etc. will automatically notify Google and Baidu.
-Integrated simple picture bed function.
-Integrated `django-compressor`, automatically compress `css`, `js`.
-Website abnormal email reminder, if there is an abnormality that is not caught, a reminder email will be sent automatically.
-Integrated WeChat official account function, now you can use WeChat official account to manage your vps.


## Installation
The mysql client is changed from `pymysql` to `mysqlclient`. For details, please refer to [pypi](https://pypi.org/project/mysqlclient/) to view the preparations before installation.

Install using pip: `pip install -Ur requirements.txt`

If you don't have pip, use the following method to install:
-OS X / Linux computer, execute under terminal:

    ```
    curl http://peak.telecommunity.com/dist/ez_setup.py | python
    curl https://bootstrap.pypa.io/get-pip.py | python
    ```

-Windows computer:

    Download http://peak.telecommunity.com/dist/ez_setup.py and https://raw.github.com/pypa/pip/master/contrib/get-pip.py these two files, double-click to run.


## Run

 Modify `DjangoBlog/setting.py` to modify the database configuration as follows:

```python
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.mysql',
        'NAME':'djangoblog',
        'USER':'root',
        'PASSWORD':'password',
        'HOST':'host',
        'PORT': 3306,
    }
}
```

### Create a database
Execute in mysql database:
```sql
CREATE DATABASE `djangoblog` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
```

Then execute in the terminal:
```bash
./manage.py makemigrations
./manage.py migrate
```

**Note:** Before using `./manage.py`, you need to make sure that the `python` command in your system points to `python 3.6` and above. If this is not the case, please use one of the following two methods:

-Modify the first line of `manage.py` `#!/usr/bin/env python` to `#!/usr/bin/env python3`
-Use `python3 ./manage.py makemigrations` directly

### Create Super User

 Execute in the terminal:
```bash
./manage.py createsuperuser
```

### Create test data
Execute in the terminal:
```bash
./manage.py create_testdata
```

### Collect static files
Execute under the terminal:
```bash
./manage.py collectstatic --noinput
./manage.py compress --force
```

### Start running:
Execute: `./manage.py runserver`


Open the browser: http://127.0.0.1:8000/ and you can see the effect.

## Server deployment

For local installation and deployment, please refer to [DjangoBlog Deployment Tutorial](https://www.lylinux.net/article/2019/8/5/58.html)
There is a detailed deployment introduction.

This project already supports the use of docker to deploy. If you have a docker environment, you can use docker to deploy. For details, please refer to: [docker deployment](/docs/docker.md)



## More configuration:
[More configuration introduction](/docs/config.md)
[Integrated elasticsearch](/docs/es.md)

## Issue related

If you have any questions, please refer to Issue, or send a description of the problem to my mailbox `liangliangyy#gmail.com`. I will answer as soon as possible. I recommend submitting the issue method.

---
 ## To everyone🙋‍♀️🙋‍♂️
 If this project helped you, please leave your URL [here](https://github.com/liangliangyy/DjangoBlog/issues/214) for more people to see.
Your reply will be my motivation to continue to update and maintain.


## Donate
If you think this project is helpful to you, you are welcome to buy me a cup of coffee. Your support is my biggest motivation. You can scan the QR code below to pay me, thank you.
### Alipay:
<div>
<img src="https://resource.lylinux.net/image/2017/12/16/IMG_0207.jpg" width="150" height="150" />
</div>

### WeChat:
<div>
<img src="https://resource.lylinux.net/image/2017/12/16/IMG_0206.jpg" width="150" height="150" />
</div>

---

Thanks jetbrains
<div>
<a href="https://www.jetbrains.com/?from=DjangoBlog"><img src="https://resource.lylinux.net/image/2020/07/01/logo.png" width= "150" height="150"></a>
</div>