import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStatePublisher(Node):
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)

        # Set the timer to publish joint states every 1 second
        self.timer = self.create_timer(1.0, self.publish_joint_state)

        # Joint names from /joint_states topic
        self.joint_names = ['base_joint', 'shoulder', 'elbow', 'wrist']
        self.joint_positions = [1.0, 1.5, 1.0, 1.5]  # Set your desired positions here

    def publish_joint_state(self):
        msg = JointState()

        # Set only the essential fields
        msg.header.stamp = self.get_clock().now().to_msg()  # Timestamp
        msg.name = self.joint_names  # List of joint names
        msg.position = self.joint_positions  # List of joint positions (angles)

        # Publish the message
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing joint states: {msg.position}")

def main(args=None):
    print("main function started")
    rclpy.init(args=args)
    joint_state_publisher = JointStatePublisher()
    rclpy.spin(joint_state_publisher)
    joint_state_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
