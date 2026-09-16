import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleDriver(Node):
    def __init__(self):
        super().__init__('circle_driver')
        self.declare_parameter('linear_speed', 1.0)
        self.declare_parameter('angular_speed', 0.9)
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.tick)
        self.get_logger().info('circle_driver started')

    def tick(self):
        msg = Twist()
        msg.linear.x = self.get_parameter('linear_speed').value
        msg.angular.z = self.get_parameter('angular_speed').value
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = CircleDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()

if __name__ == '__main__':
    main()