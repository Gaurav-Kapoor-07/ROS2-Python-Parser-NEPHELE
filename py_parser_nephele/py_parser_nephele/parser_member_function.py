import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class StringParser(Node):

    def __init__(self):
        super().__init__('parser_nephele')

        self.declare_parameter('decode_string', "x:1.0,y:1.0;x:2.0,y:2.0") # initialize string example
        self.decode_string_param = self.get_parameter('decode_string').get_parameter_value().string_value

        self.decode_string()

    def decode_string(self):
        self.get_logger().info('string received: %s' % self.decode_string_param)


def main(args=None):
    rclpy.init(args=args)

    string_parser = StringParser()

    rclpy.spin(string_parser)

    string_parser.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()