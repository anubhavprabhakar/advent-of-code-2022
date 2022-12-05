stacks=open('file1.txt', 'r')
inst=open('file2.txt', 'r')

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


#accessing each element from the array to put into particular stack
print("\nhere:")
for i in range(0, len(stc)):
    element=0
    for j in range(1, len(stc[i]), 4):
        element+=1
        print(element,":", stc[i][j], end=' ')
    print("")

print("")

print("popped:", stc)

#making into array
