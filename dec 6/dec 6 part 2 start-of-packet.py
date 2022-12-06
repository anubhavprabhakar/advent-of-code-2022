f=open('file.txt', 'r')

s=f.read()

print(s)

for i in range(0, len(s)):
    repeat = False
    for j in range(i, i+13):
        for k in range(j+1, i+14):
            if(s[j]==s[k]):
                repeat = True
                break
        if(repeat==True):
            break
        
    if(repeat==False):
        print(i+14)
        break
