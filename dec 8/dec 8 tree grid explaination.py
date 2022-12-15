grid = open('file.txt', 'r').read().split()
print(grid)
#print(len(grid[0]))

noOfRows=len(grid[0])
noOfColumns=len(grid)

edges = (noOfRows*2)+(noOfColumns*2)-4

#print(noOfRows, noOfColumns)


vis_list = []

def addToVisible(location):
    if(location not in vis_list):
        vis_list.append(location)

down_max=0
right_max=0


def up():
    for i in range(1, 
        temp=






def comparison():
    up()
    down()
    left()
    right()



def vis():
    return len(vis_list)





visibleTrees = vis() + edges
