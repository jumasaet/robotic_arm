#!/usr/bin/env python3

import rospy

from sensor_msgs.msg import JointState

global pos
pos = [0.0,0.0,0.0,0.0,0.0,0.0]

def position(state: JointState):#Recibimos del Subscriber un msg de tipo JointState y posteriormente lo publicamos con el Publisher
    global pos
    if (state.position != pos ):
        pub.publish(state)
    
    pos = state.position
    rospy.sleep(0.1)



if __name__ == "__main__":
    rospy.init_node("move_arm_node")
    pub = rospy.Publisher ("/joint_goals" , JointState, queue_size=10)
    sub = rospy.Subscriber("/joint_states", JointState, callback=position)

    rospy.logwarn("The move_arm_node has been started")
    rospy.spin()


