#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from gazebo_msgs.msg import ModelStates
import time

start_time = None
stop_time = None

def model_callback(msg):
    global start_time, stop_time

    # ตรวจสอบว่าหุ่นยนต์ตัวที่เราสนใจอยู่ที่ตำแหน่งใด
    robot1_index = msg.name.index('/')
    robot2_index = msg.name.index('spot')

    # เริ่มเวลาเมื่อหุ่นยนต์ตัวที่หนึ่งเคลื่อนที่เริ่มแล้ว
    if start_time is None and msg.twist[robot1_index].linear.x != 0.0:
        start_time = time.time()
        rospy.loginfo("Start time captured.")

    # หยุดเวลาเมื่อหุ่นยนต์ตัวที่สองไปถึงพื้นที่ที่ต้องการ
    if stop_time is None and msg.pose[robot2_index].position.x >= desired_position_x:
        stop_time = time.time()
        rospy.loginfo("Stop time captured.")

def main():
    global start_time, stop_time, desired_position_x

    rospy.init_node('time_tracker_node')

    # เลือกตำแหน่งที่หุ่นยนต์ตัวที่สองต้องไปถึง
    desired_position_x = 5.0

    rospy.Subscriber("/gazebo/model_states", ModelStates, model_callback)

    while not rospy.is_shutdown():
        if start_time is not None and stop_time is not None:
            rospy.loginfo("Time taken: {:.2f} seconds.".format(stop_time - start_time))
            break

        rospy.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
