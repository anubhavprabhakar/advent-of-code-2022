f = open('file.txt', 'r')

str=f.read()
#print(str)

a=str.split('\n')
#print(a)


def out(come):
    return {
        'A X':4,
        'A Y':8,
        'A Z':3,
        'B X':1,
        'B Y':5,
        'B Z':9,
        'C X':7,
        'C Y':2,
        'C Z':6,
        }[come]


total = 0

for i in range (0, len(a)):
    res=out(a[i])    
    total+=res

print(total)
