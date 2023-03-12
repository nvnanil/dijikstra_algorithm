import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

o_list = []
c_list = []
width = 600
height = 250
ip = True
    
fourcc = cv2.VideoWriter_fourcc(*'XVID')                    
out = cv2.VideoWriter('w_space.avi', fourcc, 20.0, (600, 250))

def goal_node(child, parent):
    if child == parent:
        return True
    
def w_space(max_x,max_y):
    #Storing points of the array into an empty list
    all_points = []
    obstacle_space = []
    p_space = [] #For storing the clearance
    for i in range(0,max_x):
        for j in range(0,max_y): 
            all_points.append((i,j)) #Appending all points to the list4
    print(len(all_points))
    for e in all_points:
        x = e[0]
        y = e[1]
    #Storing the points of the obstacle space5
    #Lower rectangle
        if x>=95 and x<=155 and y>=0 and y<=105:
            obstacle_space.append((x,y))
        elif x>=95 and x<=155 and y>=145 and y<=250:
            obstacle_space.append((x,y))
        #elif (-105*x - 60*y)-(105*455 - 60*20) <= 0 and (-105*x + 60*y)-(-105*515 + 60*125)<=0 and 210*x -(210*455)<=0:
            #obstacle_space.append((x,y))
        #elif y >= 2*x - 895 and y<=-2*x+1145 and x >= 460: useful later
            #obstacle_space.append((x,y))
        elif y >= 1.75*x - 776.25 and y <= -1.75*x + 1026.25 and x >= 455:
            obstacle_space.append((x,y))

    #Storing the points of puffed obstacle space
    for c in all_points:
        x = c[0]
        y = c[1]
    #Storing the points of the obstacle spaces
    #Lower rectangle
        if x>=100 and x<=150 and y>=6 and y<=100:
            p_space.append((x,y))
        elif x>=100 and x<=150 and y>=150 and y<=244:
            print("Good")
            p_space.append((x,y))
    #Triangle
        elif y >= 2*x - 895 and y<=-2*x + 1145 and x >= 460:
            p_space.append((x,y))
    print(len(p_space))
    return (obstacle_space,p_space)

def actions(o_list, c_list):

    child = []

    if(not ch3[int(o_list[3])][int(o_list[4])+1]): #Done
        check = np.where((c_list[:, 3] == o_list[3]) & (c_list[:, 4] == o_list[4]+1))[0]
        if(check.size==0): #Checks if no node is left in the closed list       
            child.append([o_list[0]+1,o_list[1],o_list[3],o_list[4]+1])

    if(not ch3[int(o_list[3])+1][int(o_list[4])]): #Done
        check = np.where((c_list[:, 3] == o_list[3]+1) & (c_list[:, 4] == o_list[4]))[0]
        if(check.size==0):
            child.append([o_list[0]+1,o_list[1],o_list[3]+1,o_list[4]])

    if(not ch3[int(o_list[3])][int(o_list[4])-1]): #Done
        check = np.where((c_list[:, 3] == o_list[3]) & (c_list[:, 4] == o_list[4]-1))[0]
        if(check.size==0):
            child.append([o_list[0]+1,o_list[1],o_list[3],o_list[4]-1])

    if(not ch3[int(o_list[3])-1][int(o_list[4])]): #Done
        check = np.where((c_list[:, 3] == o_list[3]-1) & (c_list[:, 4] == o_list[4]))[0]
        if(check.size==0):
            child.append([o_list[0]+1,o_list[1],o_list[3]-1,o_list[4]])

    if(not ch3[int(o_list[3])-1][int(o_list[4])+1]):  # checks if there is no obstacle #Done
        check = np.where((c_list[:, 3] == o_list[3]-1) & (c_list[:, 4] == o_list[4]+1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]-1,o_list[4]+1]) 

    if(not ch3[int(o_list[3])+1][int(o_list[4])+1]): #Done
        check = np.where((c_list[:, 3] == o_list[3]+1) & (c_list[:, 4] == o_list[4]+1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]+1,o_list[4]+1])

    if(not ch3[int(o_list[3])+1][int(o_list[4])-1]): #Done
        check = np.where((c_list[:, 3] == o_list[3]+1) & (c_list[:, 4] == o_list[4]-1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]+1,o_list[4]-1])

    if(not ch3[int(o_list[3])-1][int(o_list[4])-1]): #Done
        check = np.where((c_list[:, 3] == o_list[3]-1) & (c_list[:, 4] == o_list[4]-1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]-1,o_list[4]-1])

    return child #Contains all the generated nodes

    
obstacles, puffed = w_space(width, height)
#Defining the obstacle space
b_canvas = np.zeros((250,600,3),np.uint8)
#Puffing Walls
for i in range(5):
    for j in range(b_canvas.shape[0]):
        for k in range(b_canvas.shape[1]):
            b_canvas[j][i] = (0,0,255)
            b_canvas[i][k] = (0,0,255)
            b_canvas[b_canvas.shape[0]-1-i][k] = (0,0,255)
            b_canvas[j][b_canvas.shape[1]-1-i] = (0,0,255)
#Drawing Hexagon
corners = []
center = (300, 125)
length = 75 + 2*5*np.arctan(np.radians(30))
for i in range(6):
    x = int(center[0] + length * np.cos((i+0.5) * 2 * np.pi / 6))
    y = int(center[1] + length * np.sin((i+0.5) * 2 * np.pi / 6))
    corners.append((x, y))
hexagon = np.array(corners)
cv2.fillPoly(b_canvas, [hexagon], (0,0,255))
#ob = np.array(obstacles)
#Taking every point in the obstacle space

for c in obstacles: 
    x = c[1]
    y = c[0]
    b_canvas[(x,y)]=[0,0,255]

for l in puffed: 
    x = l[1]
    y = l[0]
    b_canvas[(x,y)]=[0,255,255]
#Flipping the image
n_canvas = b_canvas
new_canvas_copy_visited = n_canvas.copy()
#Making a copy for backtracking 
new_canvas_copy_backtrack = n_canvas.copy()
#Resizing the canvas
new_canvas_copy_visited = cv2.resize(new_canvas_copy_visited,(600,400))
#showing the obstacle map

ch1, ch2, ch3 = cv2.split(b_canvas)
ch3 = ch3.T

#Entering the input values
while ip:

    start_x= int(input("Enter the x coordinate of the start point: "))
    start_y= int(input("Enter the y coordinate of the start ponit: "))
    goal_x= int(input("Enter the x coordinate of the goal point: "))
    goal_y= int(input("Enter the y coordinate of the goal point: "))

    if (start_x > b_canvas.shape[1] or start_y > b_canvas.shape[0] or goal_x > b_canvas.shape[1] or goal_y > b_canvas.shape[0]):
        print("Invalid input, entered value outside the path space")
        print("Try Agian")
    elif ch3[start_x][start_y] == 255 or ch3[goal_x][goal_y] == 255:
        print("Invalid input, entered value in obstacle space")
        print("Try Again")
    else:
        ip = False

o_list = np.array([1,0,1,start_x,start_y])
c_list = np.array([-1,-1,-1,-1])
node_index = 1

start_time = time.time()
#Popping nodes from the open list
while( (not(c_list[-1][3]==goal_x and c_list[-1][4]==goal_y)) and (not o_list.shape[0]==0)): 
    #Sorting the existing nodes
    o_list = o_list[o_list[:,0].argsort()] 
    #Generating child nodes     
    c_node = actions(o_list[0],c_list)   

    for i in range(len(c_node)): 
        val = np.where((o_list[:, 3] == c_node[i][2]) & (o_list[:, 4] == c_node[i][3]))[0]  #Searches the open list
        if(val.size>0):
            if (c_node[i][0] < o_list[int(val)][0]):  #Compares the cost
                    o_list[int(val)][0] = c_node[i][0]  
                    o_list[int(val)][2] = c_node[i][1]   
        else:
                o_list = np.vstack([o_list, [c_node[i][0],node_index+1,c_node[i][1],c_node[i][2],c_node[i][3]]])   # add the child to open list
                node_index +=1
    #Popping element with smallest cost 
    c_list = np.vstack([c_list, o_list[0]])
    #Deleting the existing nodes
    o_list = np.delete(o_list, 0, axis=0)

print('Execuion time ' + str(time.time() - start_time) + ' sec') 
b_track = np.array([goal_x, goal_y])
val = np.where((c_list[:, 3] == goal_x) & (c_list[:, 4] == goal_y))[0]      #checks for the goal node parent
parent = c_list[int(val)][2]

while(parent):
    val = np.where(c_list[:, 1] == parent)[0]
    backtrack = np.vstack([backtrack, [c_list[int(val)][3],c_list[int(val)][4]]])
    parent = c_list[int(val)][2]

b_track = np.flip(b_track,axis = 0)
b_track = b_track.astype(int)
print("Backtracked path")
print(b_track)
cv2.circle(b_canvas, (goal_x,b_canvas.shape[0]-goal_y), 2, (255, 255, 255), 2)
cv2.circle(b_canvas, (start_x,b_canvas.shape[0]-start_y), 2, (255, 255, 255), 2)

for i in range(1,c_list.shape[0]):
    b_canvas[b_canvas.shape[0]-int(c_list[i][4])][int(c_list[i][3])][0]=255
    b_canvas[b_canvas.shape[0]-int(c_list[i][4])][int(c_list[i][3])][1]=255
    out.write(b_canvas)

for i in range(b_track.shape[0]):
    cv2.circle(b_canvas, (int(backtrack[i][0]),b_canvas.shape[0]-int(backtrack[i][1])), 1, (0, 200, 0), 1)
    out.write(b_canvas)

#cv2.imshow('Obstacle space',n_canvas)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
