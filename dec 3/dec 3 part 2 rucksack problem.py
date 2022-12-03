f = open('file.txt', 'r')

s=f.read()
a=s.split('\n')

def priority(letter):
    p = ord(letter)

    if(p<=90):
        return p-38
    else:
        return p-96


total=0


for i in range(0, len(a), 3):
    #print(i)
    string1=a[i]
    string2=a[i+1]
    string3=a[i+2]

    #print(string2)
    
    for j in range(0, len(string1)):

        #if(j>len(string2) or j>len(string3)):
            #break
        #above 2 lines are wrong, because if length of string1 exceeds string2 and string3, it still might contain the badge(required letter)
        
        if(string2.find(string1[j])!=-1):
            if(string3.find(string1[j])!=-1):
                total+=priority(string1[j])
                break

print(total)
