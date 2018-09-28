cmake_minimum_required(VERSION 2.8.3)
project(action_planning_tutorial)

find_package(catkin REQUIRED COMPONENTS
  actionlib_msgs
  rospy
# roscpp
#  test_pkg_msg
)

catkin_python_setup()

add_action_files(
  DIRECTORY action
  FILES Fibonacci.action
)

generate_messages(
  DEPENDENCIES actionlib_msgs std_msgs  # Or other packages containing msgs
)

install(PROGRAMS
  src/main.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

catkin_package(
  CATKIN_DEPENDS actionlib_msgs
)
