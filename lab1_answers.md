# Lab 1 Answers

**Name:** Athallah Ramadhan
**Student ID:** 5024241074

## Question 1
`/turtlesim` has 2 subscribers, 4 publishers, and 12 service servers. These come from `ros2 node info /turtlesim`.

## Question 2
`/turtle1/pose` publishes at a steady ~62.5 Hz because turtlesim's simulation loop runs on a fixed timer. `/turtle1/cmd_vel` fluctuates around 1.8–4.3 Hz since it's event-driven, only firing when a key is pressed in `turtle_teleop_key`.

## Question 3
A differential-drive robot can only obey `linear.x` (forward/backward) and `angular.z` (rotation); it can't obey `linear.y` because its fixed wheels can't roll sideways without slipping. Turtlesim ignores this constraint and moves sideways anyway since it's a simplified simulator, not a physically accurate one.

## Question 4
Turtlesim doesn't track who is subscribed to its topics — publishers just publish, regardless of listeners. So when the echo subscriber disconnects with Ctrl+C, turtlesim keeps publishing `/turtle1/pose` unaffected, the same way a radio station keeps broadcasting whether anyone's tuned in or not.

## Question 5
Actions add two things services lack: continuous feedback during execution and the ability to cancel mid-task. "Navigate to the kitchen" fits an action because it's long-running — you'd want progress updates and the option to cancel if something changes.

## Question 6
The package was built with `--symlink-install`, so the installed Python file is just a link to the source — since Python is interpreted, edits take effect immediately with no rebuild. If `lab1_turtle` were an `ament_cmake` C++ package, the `.cpp` would need recompiling via `colcon build` before changes show up.

## Question 7
**Cause 1:** `entry_points` in `setup.py` is missing/misspelled, so ROS 2 never registers `circle_driver` as an executable — fix by adding the correct `console_scripts` entry and running `colcon build`. **Cause 2:** the new terminal hasn't sourced the workspace — fix with `source install/setup.bash` before running `ros2 run`.
