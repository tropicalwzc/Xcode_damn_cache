
import os

Username = "tropical_fish"
aimiphonepath = "/Users/"+Username+"/Library/Developer/Xcode/iOS DeviceSupport"
aimiwatchpath = "/Users/"+Username+"/Library/Developer/Xcode/watchOS DeviceSupport"
aimdyldpath = "/Users/"+Username+"/Library/Developer/CoreSimulator/Caches/dyld"

def version_bigger_than(A,B):
    Apieces = A.split('.')
    Bpieces = B.split('.')
    print Apieces,Bpieces
    lender = min(len(Apieces),len(Bpieces))
    for l in range(lender):
        if int(Apieces[l]) < int(Bpieces[l]):
            return False
        if int(Apieces[l]) > int(Bpieces[l]):
            return True

    if len(Apieces)>len(Bpieces):
        return True
    else:
        return False

def findmaxversion(basepath):
    res = ""
    maxnum = ""
    for path in os.listdir(basepath):
        if 'DS_Store' in path:
            continue
        head = path.split('(')[0].strip().split(' ')[-1]
        if maxnum=="" or version_bigger_than(head,maxnum):
            maxnum=head
            res=path

    for path in os.listdir(basepath):
        if 'DS_Store' in path:
            continue
        if path == res:
            continue
        delete_with_rm_rf(basepath+'/'+path)

def delete_with_rm_rf(delpath):
    if os.path.exists(delpath):
        os.system("rm -rf \"" + delpath +"\"")

def del_dyld_folder():
    for folder in os.listdir(aimdyldpath):
        if 'DS_Store' in folder:
            continue

        basepath = aimdyldpath+"/"+folder
        for pth in os.listdir(basepath):
            if 'DS_Store' in pth:
                continue
            delete_with_rm_rf(basepath+"/"+pth)

if __name__ == '__main__':
    findmaxversion(aimiphonepath)
    findmaxversion(aimiwatchpath)
    del_dyld_folder()
