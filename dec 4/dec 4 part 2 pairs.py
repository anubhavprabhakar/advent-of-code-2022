f = open('file.txt', 'r')

s=f.read()
#print(str)

pairs=s.split('\n')
#print(pairs)


total=0
for i in range(0,len(pairs)):
    #print(i)
    elf1, elf2=pairs[i].split(',')
    

    astr, xstr = elf1.split('-')
    bstr, ystr = elf2.split('-')
    a=int(astr)
    b=int(bstr)
    x=int(xstr)
    y=int(ystr)

    #print(a, x, b, y)

    if(a<=y and x>=b):
        total+=1

print(total)
