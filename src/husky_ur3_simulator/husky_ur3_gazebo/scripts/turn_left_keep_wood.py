#!/usr/bin/env python3

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

def moveit_husky_ur3_pick():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('moveit_husky_ur3_pick', anonymous=True)

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    rospy.sleep(2)

    pose_target = geometry_msgs.msg.Pose()
    pose_target.orientation.w = 1.0
    pose_target.position.x = 0.5  # ตำแหน่ง x ของวัตถุ
    pose_target.position.y = 0.0  # ตำแหน่ง y ของวัตถุ
    pose_target.position.z = 0.1  # ตำแหน่ง z ของวัตถุ

    move_group.set_pose_target(pose_target)

    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()

if __name__ == '__main__':
    try:
        moveit_husky_ur3_pick()
    except rospy.ROSInterruptException:
        pass
