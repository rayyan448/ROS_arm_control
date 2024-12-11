import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/rayyan/robot_arm_ros2_ws/install/joint_state_publisher'
