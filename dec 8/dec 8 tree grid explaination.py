grid = [list(map(int, line)) for line in open('file.txt').read().splitlines()]

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



def up():
    for i in range(1, noOfRows-1):
        print('Row:', i, end=', ')
        temp = grid[0][i]
        
        for j in range(1, noOfColumns-1):
            if(grid[j][i]>temp):
                print('temp', temp, end=', ')
                temp = grid[j][i]
                print('loc: grid[',str(j)+str(i), '] tree: ', grid[j][i])
        else:
            print()
                
def down():
    for i in range(1, noOfRows-1):
        print('Row:', i, end=', ')
        temp = grid[noOfColumns-1][i]
        
        for j in range(noOfColumns-2, 0, -1):
            if(grid[j][i]>temp):
                print('temp', temp, end=', ')
                temp = grid[j][i]
                print('loc: grid[',str(j)+str(i), '] tree: ', grid[j][i])
        else:
            print()
            
def left():
    for i in range(1, noOfColumns-1):
        print('Col:', i, end=', ')
        temp = grid[i][0]
        
        for j in range(1, noOfRows-1):
            if(grid[i][j]>temp):
                print('temp', temp, end=', ')
                temp = grid[i][j]
                print('loc: grid[',str(i)+str(j), '] tree: ', grid[i][j])
        else:
            print()


def right():
    for i in range(1, noOfColumns-1):
        print('Col:', i, end=', ')
        temp = grid[i][noOfRows-1]
        
        for j in range(noOfRows-2, 0, -1):
            if(grid[i][j]>temp):
                print('temp', temp, end=', ')
                temp = grid[i][j]
                print('loc: grid[',str(i)+str(j), '] tree: ', grid[i][j])
        else:
            print()






print('\nup()')
up()
print('\n\ndown()')
down()
print('\n\nleft()')
left()
print('\n\nright()')
right()





def vis():
    return len(vis_list)





visibleTrees = vis() + edges
