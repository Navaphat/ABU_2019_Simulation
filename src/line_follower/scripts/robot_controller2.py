#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Point, Twist
import numpy as np
from sensor_msgs.msg import Image
import math
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose

class bot_control:
    def __init__(self) :
        self.velocity_msg = Twist()
        self.velocity_msg.linear.y = 0
        self.velocity_msg.linear.z = 0
        self.velocity_msg.angular.x = 0
        self.velocity_msg.angular.y = 0
        self.pub = rospy.Publisher('/spot/cmd_vel' , Twist , queue_size = 10)
        self.P = 0.004

        self.robot_names = "spot"
        self.target_points = [Pose()]

        self.target_points[0].position.x = 0.306150
        self.target_points[0].position.y = 3.350016

        self.model_state_sub = rospy.Subscriber('/gazebo/model_states', ModelStates, self.callback)

    # def callback(self, data):
    #     for i, robot_name in enumerate(self.robot_names):
    #         for j, target_point in enumerate(self.target_points):
    #             if not self.reached_targets[j]:
    #                 try:
    #                     index = data.name.index(robot_name)
    #                     robot_pose = data.pose[index]
    #                     distance_to_target = math.sqrt((robot_pose.position.x - target_point.position.x)**2 + (robot_pose.position.y - target_point.position.y)**2)
    #                     if distance_to_target < 0.5:
    #                         self.stop()
    #                 except ValueError:
    #                     pass

    

    #move function to move robot
    def move(self,linear,angular):
        self.velocity_msg.linear.x = linear + 0.2
        self.velocity_msg.angular.z = angular + 0.1
        self.pub.publish(self.velocity_msg)
        
    #fix error & bot position correction
    def fix_error(self, linear_error, orien_error):
        
        if orien_error < 0:           

            # fixing the yaw     
             self.move(0.2,self.P*orien_error + 0.6)
             #print("fixing yaw by turning left")

        elif orien_error > 0:           

            # fixing the yaw     
             self.move(0.2,self.P*orien_error)
             #print("fixing yaw by turning right")
                
        else:
            
            # moving in straight line
            self.move(0.4, 0)
            #print("moving straight")


    def callback(self, data):
        index = data.name.index(self.robot_names)
        robot_pose = data.pose[index]

        for i, target_point in enumerate(self.target_points):
            distance_to_target = math.sqrt((robot_pose.position.x - target_point.position.x)**2 + (robot_pose.position.y - target_point.position.y)**2)
            if distance_to_target < 0.5:
                self.stop()
    
    def stop(self):
         rospy.loginfo('reach the Goal.')
         rospy.signal_shutdown('Reach the Goal.')



  
if __name__=="__main__":
    robot = bot_control()
