# import os

# from ament_index_python.packages import get_package_share_directory

# from launch import LaunchDescription
# from launch.substitutions import LaunchConfiguration
# from launch.actions import DeclareLaunchArgument
# from launch_ros.actions import Node

# import xacro


# def generate_launch_description():

#     # Check if we're told to use sim time
#     use_sim_time = LaunchConfiguration('use_sim_time')

#     # Process the URDF file
#     pkg_path = os.path.join(get_package_share_directory('homebot'))
#     xacro_file = os.path.join(pkg_path,'urdf','homebot.urdf.xacro')
#     robot_description_config = xacro.process_file(xacro_file)
    
#     # Create a robot_state_publisher node
#     params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
#     node_robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         output='screen',
#         parameters=[params]
#     )


#     # Launch!
#     return LaunchDescription([
#         DeclareLaunchArgument(
#             'use_sim_time',
#             default_value='false',
#             description='Use sim time if true'),

#         node_robot_state_publisher
#     ])


from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, PathJoinSubstitution, TextSubstitution, LaunchConfiguration
from launch.conditions import IfCondition, LaunchConfigurationEquals
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(name="use_jsp", default_value="gui",
                              description="gui (default): use jsp_gui, jsp: use joint_state_publisher, none: no joint states published"),

        DeclareLaunchArgument(name="use_rviz", default_value="true",
                              description="true (default): start rviz, otherwise don't start rviz"),

        DeclareLaunchArgument(name="use_sim_time", default_value="true",),

        Node(package="joint_state_publisher_gui",
             executable="joint_state_publisher_gui",
            #  condition= LaunchConfigurationEquals("use_jsp", "gui"),
            #  parameters=[{"use_sim_time": LaunchConfiguration("use_sim_time")}],
             ),
        # Node(package="joint_state_publisher",
        #      executable="joint_state_publisher",
        #      condition= LaunchConfigurationEquals("use_jsp", "jsp")
        #      ),
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            parameters=[
                {"robot_description" :
                 Command([TextSubstitution(text="xacro "),
                          PathJoinSubstitution(
                              [FindPackageShare("homebot"), "urdf", "homebot.urdf.xacro"])])}
            ]
            ),
        Node(
            package="rviz2",
            executable="rviz2",
            arguments=["-d",
                       PathJoinSubstitution(
                           [FindPackageShare("homebot"), "rviz", "homebot.rviz"])],
            condition=LaunchConfigurationEquals("use_rviz", "true")
            )
        ])