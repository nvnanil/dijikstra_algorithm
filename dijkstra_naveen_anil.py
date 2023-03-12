import numpy as np
import cv2
import time

o_list = []
c_list = []
width = 600
height = 250
ip = True
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')                    
out = cv2.VideoWriter('w_space.avi', fourcc, 30.0, (600, 250))

def goal_node(child, parent):
    if child == parent:
        return True
    
def w_space(max_x,max_y):
    #Storing points of the array into an empty list
    all_points = []
    obstacle_space = []
    for i in range(0,max_x):
        for j in range(0,max_y): 
            all_points.append((i,j)) #Appending all points to the list
    for e in all_points:
        x = e[1]
        y = e[0]
    #Storing the points of the obstacle space
    #Defining obstacles using Half - Plane equations
    #Lower rectangle
        if y>=95 and y<=155 and x>=0 and x<=105:
            obstacle_space.append((x,y))
        elif y>=95 and y<=155 and x>=145 and x<=250: #Upper rectangle
            obstacle_space.append((x,y))
        elif x >= 1.75*y - 776.25 and x <= -1.75*y + 1026.25 and y >= 455: #Triangle
            obstacle_space.append((x,y))
        elif (y >= (235 - 5)) and (y <= (365 + 5)) and ((y + 2*x) >= 395) and ((y - 2*x) <= 205) and ((y - 2*x) >= -105) and ((y + 2*x) <= 705): #Hexagon
            obstacle_space.append((x,y))
    return (obstacle_space)

def actions(o_list, c_list): #Generating new nodes

    child = [] #For storing child nodes

    if(not ch3[int(o_list[3])][int(o_list[4])+1]): 
        check = np.where((c_list[:, 3] == o_list[3]) & (c_list[:, 4] == o_list[4]+1))[0]
        if(check.size==0): #Checks if no node is left in the closed list       
            child.append([o_list[0]+1,o_list[1],o_list[3],o_list[4]+1])

    if(not ch3[int(o_list[3])+1][int(o_list[4])]): 
        check = np.where((c_list[:, 3] == o_list[3]+1) & (c_list[:, 4] == o_list[4]))[0]
        if(check.size==0):
            child.append([o_list[0]+1,o_list[1],o_list[3]+1,o_list[4]])

    if(not ch3[int(o_list[3])][int(o_list[4])-1]): 
        check = np.where((c_list[:, 3] == o_list[3]) & (c_list[:, 4] == o_list[4]-1))[0]
        if(check.size==0):
            child.append([o_list[0]+1,o_list[1],o_list[3],o_list[4]-1])

    if(not ch3[int(o_list[3])-1][int(o_list[4])]): 
        check = np.where((c_list[:, 3] == o_list[3]-1) & (c_list[:, 4] == o_list[4]))[0]
        if(check.size==0):
            child.append([o_list[0]+1,o_list[1],o_list[3]-1,o_list[4]])

    if(not ch3[int(o_list[3])-1][int(o_list[4])+1]):  
        check = np.where((c_list[:, 3] == o_list[3]-1) & (c_list[:, 4] == o_list[4]+1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]-1,o_list[4]+1]) 

    if(not ch3[int(o_list[3])+1][int(o_list[4])+1]): 
        check = np.where((c_list[:, 3] == o_list[3]+1) & (c_list[:, 4] == o_list[4]+1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]+1,o_list[4]+1])

    if(not ch3[int(o_list[3])+1][int(o_list[4])-1]): 
        check = np.where((c_list[:, 3] == o_list[3]+1) & (c_list[:, 4] == o_list[4]-1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]+1,o_list[4]-1])

    if(not ch3[int(o_list[3])-1][int(o_list[4])-1]): 
        check = np.where((c_list[:, 3] == o_list[3]-1) & (c_list[:, 4] == o_list[4]-1))[0]
        if(check.size==0):
            child.append([o_list[0]+1.4,o_list[1],o_list[3]-1,o_list[4]-1])

    return child #Contains all the generated nodes

    
obstacles = w_space(width, height)
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

for c in obstacles: 
    x = c[0]
    y = c[1]
    b_canvas[(x,y)]=[0,0,255] #Coloring the obstacles

ch1, ch2, ch3 = cv2.split(b_canvas)
ch3 = ch3.T

print("---------------------------------------------------------")
print("Path Planner | Workspace dimensions : 250X600 pixels")

#Entering the input values
while ip:
    print("---------------------------------------------------------")
    start_x= int(input("Enter the x coordinate of the start point: "))
    start_y= int(input("Enter the y coordinate of the start ponit: "))
    goal_x= int(input("Enter the x coordinate of the goal point: "))
    goal_y= int(input("Enter the y coordinate of the goal point: "))

    if (start_x > b_canvas.shape[1] or start_y > b_canvas.shape[0] or goal_x > b_canvas.shape[1] or goal_y > b_canvas.shape[0]): #Checking whether outside the work space
        print("Invalid input, entered value outside the path space")
        print("Try Agian")
    elif ch3[start_x][start_y] == 255 or ch3[goal_x][goal_y] == 255: #Checking for obstacles
        print("Invalid input, entered value in obstacle space")
        print("Try Again")
    else:
        ip = False

o_list = np.array([[1,0,1,start_x,start_y]])
c_list = np.array([[-1,-1,-1,-1,-1]])
node_index = 1

start_time = time.time()
#Popping nodes from the open list
while( (not(c_list[-1][3]==goal_x and c_list[-1][4]==goal_y)) and (not o_list.shape[0]==0)): 
    #Sorting the existing nodes
    o_list = o_list[o_list[:,0].argsort()] 
    #Generating child nodes     
    c_node = actions(o_list[0],c_list)   

    for i in range(len(c_node)): 
        val = np.where((o_list[:, 3] == c_node[i][2]) & (o_list[:, 4] == c_node[i][3]))[0]  #Searching if child present in open list
        if(val.size>0):
            if (c_node[i][0] < o_list[int(val)][0]):  #Compares the cost
                    o_list[int(val)][0] = c_node[i][0]  
                    o_list[int(val)][2] = c_node[i][1]   
        else:
                o_list = np.vstack([o_list, [c_node[i][0],node_index+1,c_node[i][1],c_node[i][2],c_node[i][3]]])   #Adding the child to open list
                node_index +=1
    #Popping element with smallest cost 
    c_list = np.vstack([c_list, o_list[0]])
    #Deleting the existing nodes
    o_list = np.delete(o_list, 0, axis=0)

print('Execuion time ' + str(time.time() - start_time) + ' seconds') 
b_track = np.array([[goal_x, goal_y]])
val = np.where((c_list[:, 3] == goal_x) & (c_list[:, 4] == goal_y))[0]  #Checks for the goal node of the parent
parent = c_list[int(val)][2]

while(parent):
    val = np.where(c_list[:, 1] == parent)[0]
    b_track = np.vstack([b_track, [c_list[int(val)][3],c_list[int(val)][4]]])
    parent = c_list[int(val)][2]

b_track = np.flip(b_track,axis = 0)
b_track = b_track.astype(int)
print("Backtracked path:")
print(b_track)
print("Generating video....")

#Marking the start and destination points
cv2.circle(b_canvas, (goal_x,b_canvas.shape[0]-goal_y), 2, (255, 255, 255), 2)
cv2.circle(b_canvas, (start_x,b_canvas.shape[0]-start_y), 2, (255, 255, 255), 2)
#Displaying the nodes
for i in range(1,c_list.shape[0]):
    b_canvas[b_canvas.shape[0]-int(c_list[i][4])][int(c_list[i][3])][0]=200
    b_canvas[b_canvas.shape[0]-int(c_list[i][4])][int(c_list[i][3])][1]=200
    out.write(b_canvas)
#Displaying the shortest path
for i in range(b_track.shape[0]):
    cv2.circle(b_canvas, (int(b_track[i][0]),b_canvas.shape[0]-int(b_track[i][1])), 2, (200, 255, 0), 1)
    out.write(b_canvas)
out.release()
print("Video saved")
