#!/usr/bin/env python3
import subprocess

def run_script(script_number):
    if script_number == 1:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "keep_wood.py"])
    elif script_number == 2:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "close_hand_keep_wood.py"])
    elif script_number == 3:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "up_gripper.py"])
    elif script_number == 4:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "send_wood.py"])
    elif script_number == 5:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "keep_chakai.py"])
    elif script_number == 6:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "close_hand_keep_chakai.py"])
    elif script_number == 7:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "up_chakai.py"])
    elif script_number == 8:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "throw_chakai.py"])
    
    elif script_number == 9:
        subprocess.run(["rosrun", "husky_ur3_gazebo", "open_hand.py"])
    elif script_number == 10:
        subprocess.run(["rosrun", "line_follower", "line3.py"]) 
    elif script_number == 11:
        subprocess.run(["rosrun", "line_follower", "reset_spot.py"])    
    elif script_number == 12:
        subprocess.run(["rosrun", "line_follower", "line2.py"])     
    else:
        print("Invalid script number.")

if __name__ == "__main__":
    while True:
        print(" press  1     keep_stick")
        print(" press  2     close_hand_keep_stick ")
        print(" press  3     up_stick")
        print(" press  4     send_stick ")
        print(" press  5     keep_chakai ")
        print(" press  6     close_hand_keep_chakai ")
        print(" press  7     up_chakai ")
        print(" press  8     throw_chakai ")
        print(" press  9     open_hand ")
        print(" press  10    follow_line ")
        print(" press  11    reset_spot ")
        print(" press  12    follow_line_to_goal!! ")
        print(" press  0     Exit")
        
        script_number = int(input("choose Action  :"))
        if script_number == 0:
            break
        run_script(script_number)