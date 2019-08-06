## PyCharm 使用技巧记录

> ### 快捷键

#### 自动导包设置
* 在PyCHarm >Preferences >auto import 勾选show import popup
* 在 keymap >main Menu> Code >Completion>Basic 中设置 导包快捷键
* 在 file–>setting–>project:Python–>project structure 把需要导入的module(自己的) 所在目录设置为source
* 本人设置为 `shift` + `1`

#### 自动生成类中不存在的函数
* 在使用的函数处 `alt` + `enter`

> ### 配置虚拟环境
`解决不同项目对环境要求不同的方案`

* 安装python3(以python3.7为例)
* 安装virtualenvwrapper
* 新建虚拟目录(.virtualenvs),记下路径
* 对virtualenvwrapper进行配置:  
  1.进入配置文件
    ```shell script
    vi ~/.bash_profile
    ```
  2.设置变量
    ```shell script
  #virtualenvwrapper.sh文件的路径在不同的电脑上可能不一样，可以先通过      
  # sudo find / -name virtualenvwrapper.sh 查询到virtualenvwrapper.sh 文件的路径

    VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.6
    export WORKON_HOME=$HOME/.virtualenvs     #路劲可以自行更改
    source /usr/local/bin/virtualenvwrapper.sh
    ```
  3.使变量生效
    ```shell script
    source ~/.bash_profile
    
    ```
  
* 搭建虚拟环境  
`相关操作`  
```shell script
#生成新的虚拟环境
 mkvirtualenv 名称
#展示虚拟环境
 workon
#进入虚拟环境
 workon 名称
#进入虚拟环境后输入python即可开始在该环境内操作
```  

* 配合PyCharm使用

1.进入`Pycharm` -> `preference` -> `Python Interpreter` -> `show all` -> `+` ->`existing environment`
选择自己之前配置好的虚拟环境  
2自己也可以通过PyCharm对虚拟环境进行配置

