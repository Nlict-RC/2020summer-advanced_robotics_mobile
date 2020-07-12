# 2020summer-advanced_robotics_mobile
2020年暑期机器人学强化训练

* src内为基于ros的sim环境 : 需要安装的package
```bash
apt-get install ros-[version:melodic/kinetic]-[package name]
joint_state_controller velocity_controllers gazebo_ros gazebo_ros_control

apt-get install python-catkin-tools
```

* 编译
  * 安装python-catkin-tools
  * catkin build进行编译
* 运行gazebo
  * `roslaunch course_agv_gazebo course_agv_world.launch`
  * sensors包含了imu以及2d laser

![](images/1.png)

* 查看效果
  * 在gazebo开启的情况下运行`roslaunch course_agv_gazebo course_agv_world_rviz.launch`

![](images/2.png)
