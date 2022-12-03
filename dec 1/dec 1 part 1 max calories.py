f=open('file.txt', 'r')
str = f.read()
#print(str)

n=str.split('\n')

maxcals=[]

sum = 0

for i in range (0, len(n)):
    if(n[i]==''):
        maxcals.append(sum)
        sum = 0
    else:
        #print(n[i])
        num=int(n[i])
        sum+=num

maxcals.append(sum)

print("ans:", max(maxcals))
