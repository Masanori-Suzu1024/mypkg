# mypkg
千葉工業大学　2021年度ロボットシステム学で作成したROSのpackageをもとに改造したpackageです。  
  
# 動作環境n  
・Computer : Raspberry Pi 4 Computer model B   
・OS : Ubuntu 20.04 server  
・ROS ディストリビューション : melodic  

# 使用方法  
以下のコマンドを実行してください  
### インストール  
  
  ```
  $ cd ~/catkin_ws/src
  $ git clone https://github.com/Masanori-Suzu1024/mypkg.git
  $ cd ..
  $ catkin_make
  $ source ~/.bashrc
  ```  
### ROSの起動(roslaunchを使用)  
```  
$ roslaunch mypkg count.launch
```



# ライセンス  
BSD 3-Clause "New" or "Revised" License  

