#!/usr/bin/env python

from simple_pid import PID

import rospy
from geometry_msgs.msg import Point

class PointPid():
    def __init__(self):
        base = rospy.get_param("pid_param_base", 1.0)
        spz = rospy.get_param("target_altitude_from_target", 0.15)
        px = base
        py = base
        pz = base
        self.x = PID(Kp = px, Kd = px/10)
        self.y = PID(Kp = py, Kd = py/10)
        self.z = PID(Kp = pz, Kd = pz/10, setpoint = spz)

class PidNode():
    def __init__(self):
        self.pos_pid = PointPid()
        rospy.init_node('pos_error_pid', anonymous=True)
        rospy.Subscriber("/landing_pos_error/cam_frame/raw", Point, self.landing_pose_callback, queue_size=1)
        self.err_pub = rospy.Publisher("/landing_pos_error/cam_frame/pid", Point, queue_size=1)
    
    def landing_pose_callback(self, p = Point()):
        p.x = self.pos_pid.x(p.x)
        p.y = self.pos_pid.y(p.y)
        p.z = self.pos_pid.z(p.z)
        self.err_pub.publish(p)

def main():
    node = PidNode()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()