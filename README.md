# kthformula
#### Exercise 1 - ROS Network

Copy the folder to your catkin workspace's src directory. These are the commands if you want to initialize everything:
1. roscore
2. rosrun package1 nodeA.py
3. rosrun package2 nodeB.py
4. rostopic echo edgren
5. rostopic echo /kthfs/result
6. rosrun plotjuggler plotjuggler


There's probably a million reasons why the code won't work on another computer, but I can't think of any right now.

#### Exercise 2 - Visualization
So there's three different classes: PlotClass, DynamicClass, and ROSClass. The first visualizes the function provided in the assignment, the second a live-updating function, and the third the ROS network results. To change the class initialized, comment out the current function call (initially dynamic_func), and uncomment another.

It also uses tkinter (in combination with matplotlib) to:
1. Provide a field to change the "visualization name"
2. A button that saves the data with the name, date, and time to a csv file in your local folder
3. A pause, start, and restart button (that only works for DynamicClass). I also began my solution to make it work with ROSClass (by using os.system() calls and clearing the csv file where the ROS data is stored), but didn't have time to finish it.
