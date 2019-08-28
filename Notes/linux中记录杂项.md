#### 在ubuntu中记录使用linux的杂项

#### 搭建Git环境

##### 本地搭建环境
* git init   
* git config --global user.name"你的用户名"
* git config --global user.email"注册github时使用的邮箱"
* ssh-keygen -t rsa -C "13237127264@163.com"

##### 将在.ssh/下生成的id_rsa.pub 内容复制到github上,关联远程仓库
* git remote add origin git@github.com:用户名/仓库名.git

##### 在本地使用git
* git add
* git commmit
* git push
* git clone
* git fetch 配合 git reset 版本号 实现更新指定版本号到本地
* git log 配合 git branch 分支名 版本号 实现回退到指定版本号并放置到新的分支上

#### SSH代理访问

##### 配置: 在服务端  
* apt install openssh-server
* apt install openssh-client
* 修改配置文件 vi /etc/ssh/sshd_config
  Part 22
  Per....
  Pass...
* 启动服务 sshstart

##### 配置: 在访问端
* ssh 用户名@服务端ip 配合 `回车` 输入密码即可
* 若要简化操作,使用公钥和密钥实现不输入密码登录的话,需要执行以下操作

```shell script
# 注释:ssh-copy-id [-f] [-n] [-i [公钥文件路径]] [-p 端口号] [-o  ssh 选项] [user@]hostname
$ ssh-copy-id -i ~/.ssh/id_rsa.pub gustplus@192.168.1.10
```
* 以上操作会将本地主机的公钥的内容添加到远程主机指定用户home 路径下的.ssh/authorized_keys文件中

##### 操作
* 使用scp操作
* 使用使用sftp操作

