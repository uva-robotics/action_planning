#!/usr/bin/python

# ACTION PLANNING - THE TUTORIAL
#
# A nice script to do the action planning tutorial(s) in.

# Imports
import rospy
import actionlib
import action_planning_tutorial.msg

class FibonacciAction (object):
    _feedback = action_planning_tutorial.msg.FibonacciFeedback()
    _result = action_planning_tutorial.msg.FibonacciResult()

    def __init__(self.name):
        self._action_name = name
        self._as = actionlib.SimpleActionServer(self._action_name, action_planning_tutorial.msg.FibonacciAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()

    def execute_cb (self, goal):
        # helpers
        r = rospy.Rate(1)
        success = True

if __name__ == '__main__':
    print("Hello there!\nGeneral Kenobi, you are a bold one!")
