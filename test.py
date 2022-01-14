import json
import hashlib
import glob
import os

def get_md5(path):
    f1=open(path,'rb')
    md5_obj=hashlib.md5()
    while True:
        d=f1.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code=md5_obj.hexdigest()
    f1.close()
    md5=str(hash_code).lower()
    return md5
def get_dir_md5(dr,path=False):
    ans={}
    a=glob.glob(dr+'/*')
    for x in a:
        if path:
            ans[get_md5(x)]=x
        else:
            ans[get_md5(x)]=os.path.basename(x)
    return ans
if __name__=='__main__':
    audio=input('输入音频所在目录：')
    js=input('输入json文件路径：')
    f=open(js)
    d=['第四章 管道迷宫','第五章 霓虹灯牌','第六章 方舟蜃景','第七章 时钟链接','过去的章节','忘忧宫','WAVEAT精选集','Muse Dash精选集','GOOD精选集','Rising Sun Traxx精选集','HyuN精选集']
    for x in d:
        os.system('mkdir \"{}/{}\"'.format(audio,x))
    phi=json.loads(f.read())
    for x in glob.glob(audio+'/*'):
        try:
            a=get_md5(x)
            if a in phi.keys():
                os.system('mv \"{}\" \"{}/{}\"'.format(x,audio,phi[a]))
        except IsADirectoryError:
            pass
