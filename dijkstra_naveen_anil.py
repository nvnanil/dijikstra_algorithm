import numpy as np
import matplotlib.pyplot as plt
import cv2
import pygame

o_list = []
c_list = []
width = 600
height = 250

start_x= int(input("Enter the x coordinate of the start point: "))
start_y= int(input("Enter the y coordinate of the start ponit: "))
goal_x= int(input("Enter the x coordinate of the goal point: "))
goal_y= int(input("Enter the y coordinate of the goal point: "))


def goal_node(child, parent):
    if child == parent:
        return True
    
def dijkstra(Maximum_size_x,Maximum_size_y,start,goal):
    #Storing points of the array into an empty list
    all_points = []
    obstacle_space = []
    p_space = []
    for i in range(0,600):
        for j in range(0,250): 
            all_points.append((i,j)) #Appending all points to the list4
    print(len(all_points))
    for e in all_points:
        x = e[0]
        y = e[1]
    #Storing the points of the obstacle space5
    #Lower rectangle
        if x>=95 and x<=155 and y>=0 and y<=105:
            obstacle_space.append((x,y))
        elif x>=100 and x<=150 and y>=0 and y<=100:
            print("Good")
            p_space.append((x,y))
        elif x>=95 and x<=155 and y>=145 and y<=250:
            obstacle_space.append((x,y))

    for c in all_points:
        x = c[0]
        y = c[1]
    #Storing the points of the obstacle space5
    #Lower rectangle
        if x>=100 and x<=150 and y>=0 and y<=100:
            p_space.append((x,y))
        elif x>=100 and x<=150 and y>=150 and y<=250:
            print("Good")
            p_space.append((x,y))
    print(len(p_space))
    return (obstacle_space,p_space)

    if goal in obstacle_space:
        print("The entered goal is in the obstacle space, run again")

obstacles, puffed = dijkstra(width, height, start_x, start_y)
#print(obstacles)
#print("Puffed", len(puffed))

b_canvas = np.zeros((250,600,3),np.uint8) 
#Taking every point in the obstacle space
for c in obstacles: 
    x = c[1]
    y = c[0]
    b_canvas[(x,y)]=[255,0,0]
for l in puffed: 
    x = l[1]
    y = l[0]
    b_canvas[(x,y)]=[0,255,0]
#Flipping the image
n_canvas = np.flipud(b_canvas)
new_canvas_copy_visited = n_canvas.copy()
#Making a copy for backtracking 
new_canvas_copy_backtrack = n_canvas.copy()
#Resizing the canvas
new_canvas_copy_visited = cv2.resize(new_canvas_copy_visited,(600,400))
#showing the obstacle map
cv2.imshow('Obstacle space',n_canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
