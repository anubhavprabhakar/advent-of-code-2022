terminal=open('file.txt', 'r').read().split('\n')
terminal.reverse()
print(terminal, "\n")

sizeofdir={'/':0}

def dirsize(name):
    return(sizeofdir[name])


def makesizelist(string):
    size = 0
    for i in range(0, len(string)):
        s=string[i].split()
        print(s)
        
        
        if(s[0]=='$'):
            if(s[1]=='ls'):
                continue
            if(s[1]=='cd' and s[2]=='..'):
                continue
            else:
                if(s[2] not in sizeofdir.keys()):
                    dic = {s[2]: 0}
                    sizeofdir.update(dic)
                sizeofdir[s[2]]+=size
                size = 0
                continue
            
        
        if(s[0].isdigit()):
            size+=int(s[0])
            #print('add')
            continue
        if(s[0]=='dir'):
            size+=dirsize(s[1])
            #print('add')


makesizelist(terminal)

print("\n",sizeofdir)
