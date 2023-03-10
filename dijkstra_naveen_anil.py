import numpy as np
import matplotlib.pyplot as plt
import cv2

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

b_canvas = np.zeros(250,600)
