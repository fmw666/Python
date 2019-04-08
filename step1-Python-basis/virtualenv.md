## 开启本地虚拟环境
+ 安装virtualenv
  ```python
  pip install virtualenv
  ```
  
+ 创建虚拟环境

  在文件夹下执行终端：
  ```python
  virtualenv mysite_env
  ```
  ```shell
  $ cd mysite_env
  $ Scripts\activate
  (mysite_env)安装需要包
  ```
  
+ 退出虚拟环境
  ```python
  deactivate
  ```
+ pip一键导出和安装
  ```python
  pip freeze > requirements.txt
  pip install -r requirements.txt
  ```
