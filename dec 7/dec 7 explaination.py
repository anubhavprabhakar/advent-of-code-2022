#make sure to change file.txt to the example given on website to understand better

terminal=open('file.txt', 'r').read().split('\n')
terminal.reverse()  #terminal output is reversed to better calculate the size of a directory(not needed to do it recursively),
                    #and just add that size when 'dir <name>' is there in its parent directory

print(terminal, "\n")

sizeofdir={}

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
                if(s[2] in sizeofdir.keys()):
                    s[2]=s[2]+'copy'    # if dir with same name exists in key, then simply change its name to '<name>copy'
                    dic = {s[2]: 0}
                    sizeofdir.update(dic)
                    sizeofdir[s[2]]+=size
                    size = 0
                    continue
                else:
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
