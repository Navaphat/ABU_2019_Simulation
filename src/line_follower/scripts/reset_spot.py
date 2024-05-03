#!/usr/bin/python3


import rospy
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose, Twist

def set_model_state():
    rospy.init_node('set_model_state_node', anonymous=True)
    pub = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
    rospy.sleep(1)  # Wait for publisher to initialize

    model_state = ModelState()
    model_state.model_name = 'spot'

    # Set desired pose
    model_state.pose = Pose()
    model_state.pose.position.x = 0.295861
    model_state.pose.position.y = 3.336597
    model_state.pose.position.z = 0.493333
    model_state.pose.orientation.x = -0.005400
    model_state.pose.orientation.y = 0.008117
    model_state.pose.orientation.z = 1
    model_state.pose.orientation.w = 1.0


    rospy.loginfo("Setting model state...")
    pub.publish(model_state)
    rospy.loginfo("Model state set successfully.")

if __name__ == '__main__':
    try:
        set_model_state()
    except rospy.ROSInterruptException:
        pass
