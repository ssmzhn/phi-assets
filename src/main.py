import glob
import os
f=open('..\\philist.txt')
f1=open('..\\added.txt','w')
added=''
philist=f.read().splitlines()
ls=glob.glob('*')
for x in ls:
    ls1=x+'\\'+glob.glob(x+'\\*')
    for y in ls1:
        a=os.popen('certutil -hashfile '+y+' MD5').read().splitlines()[1]
        for z in philist():
            if z.find(a)==-1:
                added+=(z+'\n')
f1.write(added)
f1.close()
