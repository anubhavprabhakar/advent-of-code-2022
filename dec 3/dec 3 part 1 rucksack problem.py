f = open('file.txt', 'r')

s=f.read()
#print(str)

a=s.split('\n')
#print(a[0])

def priority(letter):
    p = ord(letter)

    if(p<=90):
        return p-38
    else:
        return p-96

#print(priority('z'))


#ch = a[0][len(a[0])//2:]
#print('bfdjksa'.find('a'))
#print(ch)


total=0


for i in range(0, len(a)):
    #checked=[]
    #print("chk: ", checked)
    string1=a[i][:len(a[i])//2]
    string2=a[i][len(a[i])//2:]
    for j in range(0, len(string1)):
        #try:
            #if(checked.index(string1[j])):
        if(string2.find(string1[j])!=-1):
            #print(priority(string1[j]), " ", string1[j])
            total+=priority(string1[j])
            break
        #except ValueError:
            #checked.append(string1[j])
    #print("fin: ", checked)


print(total)
