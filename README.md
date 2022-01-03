# mypkg
千葉工業大学　2021年度ロボットシステム学で作成したROSのpackageをもとに改造したpackageです。  
原神のダメージ計算ツールと簡易的なトータルダメージシミュレータです  
  
# 動作環境  
・Computer : Raspberry Pi 4 Computer model B   
・OS : Ubuntu 20.04 server  
・ROS ディストリビューション : melodic  

# 使用方法  
端末を2つ用意し、以下のコマンドを実行してください  
### インストール  
  
  ```
  $ cd ~/catkin_ws/src
  $ git clone https://github.com/Masanori-Suzu1024/mypkg.git
  $ cd ..
  $ catkin_make
  $ source ~/.bashrc
  ```  
### ROSの起動(roslaunchを使用) (端末1) 
```  
$ roslaunch mypkg count.launch
```
### ROSTOPICの表示(端末2)
```  
$ cd catkin_ws  
$ rostopic echo /twice  
```  
### 以下の

# ライセンス  
BSD 3-Clause "New" or "Revised" License  

