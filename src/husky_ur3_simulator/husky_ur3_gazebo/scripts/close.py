#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def gripper_control():
    # เริ่มต้นโหนด ROS ใหม่
    rospy.init_node('gripper_controller', anonymous=True)

    # สร้าง publisher เพื่อส่งคำสั่งไปยัง gripper
    gripper_pub = rospy.Publisher('/gripper_control', String, queue_size=10)

    # แสดงคำแนะนำสำหรับผู้ใช้
    rospy.loginfo("ใช้ 'o' เพื่อเปิด gripper และ 'c' เพื่อปิด gripper")

    # รอรับข้อมูลจากคีย์บอร์ดและส่งคำสั่งไปยัง gripper
    while not rospy.is_shutdown():
        command = input("Enter 'o' to open gripper or 'c' to close gripper: ")
        if command.lower() == 'o':
            gripper_pub.publish("open")
        elif command.lower() == 'c':
            gripper_pub.publish("close")
        else:
            rospy.logwarn("Invalid command! Please enter 'o' to open gripper or 'c' to close gripper.")

if __name__ == '__main__':
    try:
        gripper_control()
    except rospy.ROSInterruptException:
        pass
