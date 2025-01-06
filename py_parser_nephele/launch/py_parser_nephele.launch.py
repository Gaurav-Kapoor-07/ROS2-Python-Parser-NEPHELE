from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    passed_string = "x:2.0,y:2.0;x:1.0,y:1.0"

    return LaunchDescription([

        Node(
            package='py_parser_nephele',
            executable='parser_nephele',
            name='parser_nephele',
            # namespace='summit',
            parameters=[{"decode_string": passed_string}, {"use_sim_time": True}],
            output='screen',
            remappings=[('/tf', '/summit/tf'), ('/tf_static', '/summit/tf_static')],
            emulate_tty=True,
        ),
    ])
