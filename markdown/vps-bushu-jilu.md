VPS部署记录
====

前两天匆匆忙忙部署了个网站，用的都是最传统的东西centos+httpd+php+mysql。这些东西都可以通过yum来安装，比较省事。

另外代码提交直接是搭了个svn仓库，然后通过hook来同步网站内容，这样修改起来方便很多。

下面记录一些怕忘记的东西。

## apache httpd 配置

直接在`/etc/httpd/conf.d`中增加一个配置文件就行，类似这样
	
	<VirtualHost *:80>
	    ServerAdmin   admin@test.com
	    DocumentRoot  /var/www/html/test 
	    ServerName   test.com
	    ErrorLog  logs/test-error_log
	    CustomLog logs/test-access_log common
	</VirtualHost>

## mysql

### 初始化配置

安装完后运行`mysql_secure_installation`这个向导就可以了。

### 启动服务

`sudo service mysqld start`

### 开机自启动

这个还没弄

### 数据库管理工具

本来想直接yum安装phpmyadmin，但是总有一些问题，后面发现一个[adminer](https://www.adminer.org/)只要单个php文件就行了，很方便，官网下载放上去就行了。

### svn仓库

这个有点繁琐，也可以随时百度一些教程，先讲讲大概过程。

#### 创建代码仓库

`svnadmin create /path/of/reposdir`

#### 配置svn仓库参数

**passwd**

	[users]
	hello=123

**authz**
	
	[/]
	hello=rw

**snvserv.conf**
	anon-access = none # 使非授权用户无法访问
	auth-access = write # 使授权用户有写权限
	password-db = password
	authz-db = authz   # 访问控制文件
	realm = /opt/svn/repos # 认证命名空间，一般仓库的路径即可

#### 启动服务

	svnserve -d -r ./svnrepos

