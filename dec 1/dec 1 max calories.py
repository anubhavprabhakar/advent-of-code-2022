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

maxcals.sort(reverse=True)
#top3 = sorted(maxcals)

#print(top3)

sum = 0

for i in range(1, 4):
    #print(maxcals[-i])
    sum+=maxcals[-i]

print("ans:", sum)
