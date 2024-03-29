# 记录一些在 VPS 上折腾的东西

折腾这些东西，总是要经常借助搜索引擎找答案，找的次数多了，也就烦了，不想总是做重复工作。

所以把做过的一些事情记录一下，加深一下印象。

## 1、安装 python2.7

VPS 上面的太老了，之前安装的，过程暂时不记得了，无非就是去 python 官网下载源码，然后编译，然后安装。

安装完后把原来的/usr/bin/python 重命名一下，然后用 ln 命令把/usr/local/bin/python 链到/usr/bin/python 下，这样直接输 python 就可以用 2.7 了。

## 2、安装 pip

但是这样默认的 pip 还是旧的，直接使用会有`No module named pkg_resources`的问题。搜索一圈答案，感觉这个比较靠谱：[http://my.oschina.net/dlpinghailinfeng/blog/203015](http://my.oschina.net/dlpinghailinfeng/blog/203015)

但是这里面提供的 distribute_setup.py 似乎失效了，所以去这里[https://pypi.python.org/pypi/distribute/0.6.49](https://pypi.python.org/pypi/distribute/0.6.49)下载，解压，执行：

```bash
    python distribute_setup.py
    easy_install pip
```

pip 也就安装好了

## 3、安装 Mysql

首先`yum list|grep mysql`一下，看看有哪些 mysql 相关的包。

据说得安装这些：

```bash
yum install -y mysql mysql-server mysql-devel
```

然后就可以`service mysqld start`启动 mysql 服务了，根据提示进行一些配置即可。

感觉执行`mysql_secure_installation`这个向导就不错
