
# Unitree package
#cd /home/ros1_ws/src/unitree
#git clone https://github.com/unitreerobotics/unitree_ros.git
#git clone -b v3.2.1 https://github.com/unitreerobotics/unitree_ros_to_real.git
#git clone -b v3.2 https://github.com/unitreerobotics/unitree_legged_sdk.git
#cd ../../
#catkin build

# Install package
apt update
apt install -y ros-melodic-controller-interface  ros-melodic-gazebo-ros-control ros-melodic-joint-state-controller ros-melodic-joint-state-publisher-gui ros-melodic-effort-controllers ros-melodic-joint-trajectory-controller
apt install -y x11-apps


# Assign enviroment variables
export ROS_PACKAGE_PATH=/home/ros1_ws:${ROS_PACKAGE_PATH}
export GAZEBO_PLUGIN_PATH=/home/ros1_ws/devel/lib:${GAZEBO_PLUGIN_PATH}
export LD_LIBRARY_PATH=/home/ros1_ws/devel/lib:${LD_LIBRARY_PATH}
export UNITREE_SDK_VERSION=3_2
export UNITREE_LEGGED_SDK_PATH=/home/ros1_ws/src/unitree/unitree_legged_sdk
export UNITREE_PLATFORM="amd64"

# Install lcm of cpp library for unitree_legged_sdk
mkdir /home/cpp_build && cd /home/cpp_build
git clone -b v1.4.0 https://github.com/lcm-proj/lcm.git
cd /home/cpp_build/lcm
mkdir build && cd build/
cmake ..
make
make install

# Build unitree_legged_sdk
mkdir -p /home/ros1_ws/src/unitree/unitree_legged_sdk/build
cd /home/ros1_ws/src/unitree/unitree_legged_sdk/build
cmake ..
make

# Setting network
cd /
chmod 777 /home/ros1_ws/src/unitree/unitree_ros_to_real/unitree_legged_real/ipconfig.sh
#vi /etc/network/interfaces

# ROS build
cd /home/ros1_ws
catkin build