#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_command():
    rospy.init_node('command_publisher', anonymous=True)
    pub = rospy.Publisher('/rh_p12_rn_position/command', Float64, queue_size=10)
    rospy.sleep(1)  # Sleep for 1 second to allow publisher to register

    data = 0.0
    msg = Float64(data=data)

    rate = rospy.Rate(1)  # 1 Hz
    timeout = rospy.Duration.from_sec(1)  # Timeout after 10 seconds
    start_time = rospy.Time.now()

    while not rospy.is_shutdown() and rospy.Time.now() - start_time < timeout:
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_command()
    except rospy.ROSInterruptException:
        pass
        