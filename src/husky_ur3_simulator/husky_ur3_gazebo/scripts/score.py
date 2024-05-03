#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose
import math

class RobotController:
    def __init__(self):
        rospy.init_node('robot_controller', anonymous=True)
        self.robot_names = ["/", "spot"]  # ชื่อของหุ่นยนต์ใน Gazebo
        self.target_points = [Pose(), Pose(), Pose(), Pose(), Pose(), Pose() , Pose()]  # จุดที่ต้องการให้หุ่นยนต์เดินไป
        # จุดที่ 1
        self.target_points[0].position.x = 10.188890  # ตำแหน่ง x ของจุดเป้าหมายที่ 1
        self.target_points[0].position.y = 4.625933  # ตำแหน่ง y ของจุดเป้าหมายที่ 1
        
        # จุดที่ 2
        self.target_points[1].position.x = 7.117414 # ตำแหน่ง x ของจุดเป้าหมายที่ 2
        self.target_points[1].position.y = 5.989498  # ตำแหน่ง y ของจุดเป้าหมายที่ 2
       
        # จุดที่ 3
        self.target_points[2].position.x = 4.867460  # ตำแหน่ง x ของจุดเป้าหมายที่ 3
        self.target_points[2].position.y = 5.817140  # ตำแหน่ง y ของจุดเป้าหมายที่ 3
        
        # จุดที่ 4
        self.target_points[3].position.x = 3.233231  # ตำแหน่ง x ของจุดเป้าหมายที่ 4
        self.target_points[3].position.y = 4.026143  # ตำแหน่ง y ของจุดเป้าหมายที่ 4
        
        # จุดที่ 5
        self.target_points[4].position.x = 0.253508  # ตำแหน่ง x ของจุดเป้าหมายที่ 5
        self.target_points[4].position.y = 3.314193  # ตำแหน่ง y ของจุดเป้าหมายที่ 5

        # จุดที่ 6
        self.target_points[5].position.x = 4.960384  # ตำแหน่ง x ของจุดเป้าหมายที่ 5
        self.target_points[5].position.y = 4.117836  # ตำแหน่ง y ของจุดเป้าหมายที่ 5

        # จุดที่ 7
        self.target_points[6].position.x = 0.202972  # ตำแหน่ง x ของจุดเป้าหมายที่ 5
        self.target_points[6].position.y = 6.643107  # ตำแหน่ง y ของจุดเป้าหมายที่ 5
        
        self.model_states_subscriber = rospy.Subscriber('/gazebo/model_states', ModelStates, self.model_states_callback)
        self.scores = [0, 0]  # คะแนนของทั้งสองหุ่นยนต์
        self.reached_targets = [False] * len(self.target_points)  # แสดงถึงว่าแต่ละจุดเป้าหมายถูกเดินผ่านไปแล้ว

    def model_states_callback(self, data):
        for i, robot_name in enumerate(self.robot_names):
            for j, target_point in enumerate(self.target_points):
                if not self.reached_targets[j]:
                    try:
                        index = data.name.index(robot_name)
                        robot_pose = data.pose[index]
                        distance_to_target = math.sqrt((robot_pose.position.x - target_point.position.x)**2 +
                                                       (robot_pose.position.y - target_point.position.y)**2 )
                        if distance_to_target < 0.5:  # ถ้าหุ่นยนต์เคลื่อนที่มาถึงจุดเป้าหมาย
                            if j < 2:
                                self.scores[i] += 20  # เพิ่มคะแนน 20 คะแนน
                            elif j < 5:
                                self.scores[i] += 30  # เพิ่มคะแนน 30 คะแนน
                            elif j< 6:
                                self.scores[i] += 50  # เพิ่มคะแนน 50 คะแนน
                            else:
                                self.scores[i] += 30  # เพิ่มคะแนน 30 คะแนน
                            rospy.loginfo("หุ่นยนต์ตัวที่  %d ผ่านจุดที่ %d. ได้คะแนน: %d", i+1, j+1, self.scores[i])
                            rospy.loginfo("คะแนนรวมเป็น: %d", sum(self.scores))  # แสดงคะแนนรวม
                            self.reached_targets[j] = True
                    except ValueError:
                        pass  

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    controller = RobotController()
    controller.run()
