## Contributors
- Sameep Pote - M.Eng. Robotics Student at University of Maryland College Park. 
- Atharva Paralikar - M.Eng. Robotics Student at University of Maryland College Park. 

### Videos
Video 1: https://youtu.be/9r2kkl5v4UA
Video 2: https://youtu.be/M6V7ly5J5zk 

## Steps to Run Program
Copy the file present in the package in your src of catkin workspace (/home/User_name/catkin_ws/src/..)
Then build project
```
cd catkin_ws
catkin_make clean && catkin_make
source  ~/catkin_ws/devel/setup.bash
```
Once the build is done we can run the 
```
roscore
```
In a new terminal tab
```
roslaunch proj1_assembly template_launch.launch
```
This will launch the package in the gazebo world
Next to control your robot using teleop
```
cd /home/User_name/catkin_ws/src/proj1_assembly/src
chmod +x teleop.py
python3 teleop.py
```
