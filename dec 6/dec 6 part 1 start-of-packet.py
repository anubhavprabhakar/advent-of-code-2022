f=open('file.txt', 'r')

s=f.read()

print(s)

for i in range(0, len(s)):
    repeat = False
    if(s[i]==s[i+1] or s[i]==s[i+2] or s[i]==s[i+3]):
        repeat=True
    if(repeat==False):
        if(s[i+1]==s[i+2] or s[i+1]==s[i+3]):
            repeat=True

        if(repeat==False):
            if(s[i+2]==s[i+3]):
                repeat=True

    if(repeat==False):
        print(i+4)
        break
