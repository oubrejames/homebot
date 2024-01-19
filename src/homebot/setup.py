from setuptools import setup

package_name = 'homebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/rviz', ['rviz/homebot.rviz']),
        ('share/' + package_name + '/launch', ['launch/state_pub.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/homebot.urdf.xacro', 'urdf/homebot_core.xacro']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='oubre',
    maintainer_email='oubrejames@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
