

$  git clone https://github.com/Navaphat/ABU_2019_Simulation.git

  
** warning**
install _descriptions
$  cd ABU_2019_Simulation/src/robots
$  ./install_descriptions
$  cd ~/ABU_2019_Simulation/ && catkin_make
$  . devel/setup.bash

-------------------------------------------------------------------------------------------------------

 นำ folder src จาก folder place ทำการ copy มา replace ใน work space ชื่อ ABU_2019_Simulation เพื่อปรับการตั้งค่าและติดตั้งเเขนกลของหุ่นยนต์ spot 
 -------------------------------------------------------------------------------------------------------  
   
Run Project
$  cd ABU_2019_Simulation
$  . devel/setup.bash
$  roslaunch husky_ur3_gazebo husky_ur3.launch

-------------------------------------------------------------------------------------------------------

การคิดคะแนน 
เปิด new tap Terminal Run คำสั่ง
$  cd ABU_2019_Simulation
$  . devel/setup.bash
$  rosrun husky_ur3_gazebo score.py
 -------------------------------------------------------------------------------------------------------
ควบคุมการเคลื่อนที่ของหุ่นยนตบังคับมือ 
เปิด new tap Terminal Run คำสั่ง
$  sudo apt-get install ros-noetic-teleop-twist-keyboard
$  cd ABU_2019_Simulation
$  . devel/setup.bash
$  rosrun teleop_twist_keyboard teleop_twist_keyboard.py	
 -------------------------------------------------------------------------------------------------------
 
ควบคุมแขนกล, Gripper, ควบคุมการเคลื่อนที่ของหุ่นยนต์อัตโนมัติ
เปิด new tap Terminal Run คำสั่ง
$  cd ABU_2019_Simulation
$  . devel/setup.bash
$  rosrun husky_ur3_gazebo main_run.py

สามารถควบคุมหุ่นยนต์อัตโนมัติโดยการ เลือก press 10, 11, 12
-----------------------------------------------------------------------------------------------------

 Bring up MoveIt & RViz หุ่นยนต์บังคับมือ
$  cd ABU_2019_Simulation
$  . devel/setup.bash
$  roslaunch husky_ur3_gripper_moveit_config Omni_control.launch
 
-----------------------------------------------------------------------------------------------------
 
Scripts การควบคุมแขนหุนยนต์บังคับมือเก็บไว้ที่ :
Path: ABU_2019_Simulation/src/husky_ur3_simulator/husky_ur3_gazebo/scripts
 
-----------------------------------------------------------------------------------------------------
 
Scripts การควบคุมการเดินของหุนยนต์อัตโนมัติเก็บไว้ที่
Path: ABU_2019_Simulation/src/line_follower/scripts
 
-----------------------------------------------------------------------------------------------------
 
Model สนามการเเข่งขัน, ไม้ผลัด, ชาไก เก็บไว้ที่
Path: ABU_2019_Simulation/src/line_follower/models
 
-----------------------------------------------------------------------------------------------------
 
การติดตั้งแขนหุ่นยนต์อัตโนมัติสามารถไปแก้ไขไฟล์ spot.urdf ได้ที่
 Path: ABU_2019_Simulation/src/robots/descriptions/spot_ros/spot_description/urdf
 
-----------------------------------------------------------------------------------------------------
Folder gazebo-pkgs ที่อยู่ใน src จะเก็บ plugin ที่ทำให้สามารถจับวัตถุได้
Folder champ ที่อยู่ใน src จะใช้ในการควบคุม Joint ของหุ่นยนต์อัตโนมัติ
Folder champ_setup_assistant ที่อยู่ใน src จะใช้ในการตั้งค่าหุ่นยนต์อัตโนมัติ
 
 
 
 
 
 
 
 
 
 
 
 
 
