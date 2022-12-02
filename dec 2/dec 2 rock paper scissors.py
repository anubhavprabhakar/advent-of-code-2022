f = open('file.txt', 'r')

str=f.read()
#print(str)

a=str.split('\n')
#print(a[0][2])


def out(come):
    return {
        'A X':3,
        'A Y':4,
        'A Z':8,
        'B X':1,
        'B Y':5,
        'B Z':9,
        'C X':2,
        'C Y':6,
        'C Z':7,
        }[come]


total = 0
for i in range (0, len(a)):
    res=out(a[i])    
    total+=res

print(total)
