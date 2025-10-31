# launch/webrtc.launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            "robot_id",
            default_value="6904029f67871d8428227b86",
            description="Unique ID of the robot"
        ),
        DeclareLaunchArgument(
            "signaling_url",
            default_value="wss://10.0.0.69:3000/signal",
            description="WebSocket URL of the signaling server"
        ),
        DeclareLaunchArgument(
            "auth_token",
            default_value="",
            description="Optional auth token for signaling server"
        ),

        Node(
            package="webrtc",
            executable="webrtc_node",
            name="webrtc_client",
            output="screen",
            parameters=[{
                "robot_id": LaunchConfiguration("robot_id"),
                "signaling_url": LaunchConfiguration("signaling_url"),
                "auth_token": LaunchConfiguration("auth_token"),
            }],
        ),
    ])
