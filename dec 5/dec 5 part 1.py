stacks=open('file1.txt', 'r')
inst=open('file2.txt', 'r')

ins = inst.read()
s = stacks.read()


#storing in list format
stc = s.split('\n')


#for getting number of stacks
nums=stc.pop()
numOfStc=int(nums[-2])

arr=[]
d={}

#accessing each element from the stacks(in the rocket ship) to put into particular list

for i in range(0, len(stc)):
    element=0   #to know which stack the following element belongs to
    for j in range(1, len(stc[i]), 4):
        element+=1
        if(stc[i][j]!=' '):
            if element not in d.keys():
                dic={element: []}
                d.update(dic)
            d[element].append(stc[i][j])
                


#to reverse the list of stacks, so that popping and appending operations give correct representation of items moved
for i in range(1, numOfStc+1):
    d[i].reverse()


#accessing instructions
ins=ins.split('\n')

#print(ins)

for i in range(0, len(ins)):
    instruction = ins[i].split()

    #so the instruction is in the form of 'move X' 'from X' 'to X', hence naming the variables    
    move = int(instruction[1])
    _from = int(instruction[3])
    to = int(instruction[5])

    for j in range(0, move):  #moving 'move' number of times
        toMove=d[_from].pop() #popping top most element, i.e. the last element from the 'from' list
        d[to].append(toMove)  #placing that element into the 'to' list it asked(the instruction asked)


#print(d)

for i in range(1, numOfStc+1):
    print(d[i][-1], end="")



        
