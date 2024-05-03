#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def publish_command(hand_state):
    rospy.init_node('command_publisher', anonymous=True)
    pub = rospy.Publisher('/rh_p12_rn_position/command', Float64, queue_size=10)
    rospy.sleep(1)  # Sleep for 1 second to allow publisher to register

    if hand_state == 1:
        data = 1.0  # Open the hand
    elif hand_state == 2:
        data = 0.0  # Close the hand
    else:
        rospy.logerr("Invalid hand state command. Please enter 1 to open or 2 to close.")
        return

    msg = Float64(data=data)

    rate = rospy.Rate(1)  # 1 Hz
    timeout = rospy.Duration.from_sec(1)  # Timeout after 1 second
    start_time = rospy.Time.now()

    while not rospy.is_shutdown() and rospy.Time.now() - start_time < timeout:
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        user_input = int(input("Enter 1 to open the hand or 2 to close the hand: "))
        publish_command(user_input)
    except rospy.ROSInterruptException:
        pass
    except ValueError:
        rospy.logerr("Invalid input. Please enter either 1 or 2.")

