f = open('file.txt', 'r')

s=f.read()
#print(str)

pairs=s.split('\n')
#print(pairs)

# elf1, elf2=pairs[0].split(',')
# print(elf1, elf2)
# a, x = (elf1.split('-')
# print(a, x)
# a=int(a)
# print(type(a))


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

    if(a==b or x==y):
        total+=1
        continue
    else:
        if(a>b and x<y):
            total+=1
            continue
        if(a<b and x>y):
            total+=1
            continue

print(total)
