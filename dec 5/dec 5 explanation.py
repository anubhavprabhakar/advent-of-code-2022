#to understand well, insert the example in file1.txt(the figure of stacks) and file2.txt(the instructions)
#make sure to remove extra blank lines(and not extra spaces after or in between any line, for both stack diagram and instructions)

stacks=open('file1.txt', 'r')
inst=open('file2.txt', 'r')

ins = inst.read()
s = stacks.read()

#for i in range(0, len(s)):
    #print(i)

print("s:")
print(s)

#storing in list format
stc = s.split('\n')
print("stack:", stc)

#for getting number of stacks
nums=stc.pop()
print("popped nos:", nums)
numOfStc=int(nums[-2])


d={}

#making stacks into array/dictionary

#accessing each element from the stacks(in the rocket ship) to put into particular list
print("\nhere:")
for i in range(0, len(stc)):
    element=0   #to know which stack the following element belongs to
    for j in range(1, len(stc[i]), 4):
        element+=1
        print(element,":", stc[i][j], end=' ')
        if(stc[i][j]!=' '):  #to ignore the blank space instead of a crate
            if element not in d.keys():
                dic={element: []}
                d.update(dic)
            d[element].append(stc[i][j])
            
            
    print("")

#to reverse the list of stacks, so that popping and appending operations give correct representation of items moved
for i in range(1, numOfStc+1):
    d[i].reverse()

print("dictionary: ", d)

print("")

print("popped:", stc)



#accessing instructions
ins=ins.split('\n')

print(ins)

for i in range(0, len(ins)):
    instruction = ins[i].split()
    print(instruction)  
    move = instruction[1]
    _from = instruction[3]
    to = instruction[5]

    print(move, _from, to)

    
    
    
