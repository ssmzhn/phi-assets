f_168=open('philist-v1.6.8.txt')
f_1611=open('philist-v1.6.11.txt')
ls8=f_168.read().splitlines()
ls11=f_1611.read().splitlines()
add=''
for x in ls8:
    for y in ls11:
        if x.find(y.split()[0])==-1:
            add+=(y+'\n')
f=open('added.txt','w')
f.write(add)
f.close()
