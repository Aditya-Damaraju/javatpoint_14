import math
train1_length = int(input("Enter the length of train 1:"))
train1_speed = int(input("Enter the speed of train 1:"))
train2_speed = int(input("Enter the speed of train 2:"))
time = int(input("Enter the time for crossing:"))
relative_speed = train1_speed + train2_speed
r_s = relative_speed * 5/18
x = print("Let x be the length of the train 2")
x = (r_s * time) - 150
print("Length of Train 2 is:", x)
exit (0)
