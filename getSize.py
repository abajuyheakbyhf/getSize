import os

num = 0
flist = []
cntn = []
cnts = []

a = input()
os.chdir(a)

flist = os.listdir(a)

def setList(s,ilist):
    os.chdir(s)
    glist = []
    
    for i in range(len(ilist)):
        if os.path.isdir(ilist[i]):
            cntn.append(i)
            cnts.append(ilist[i])
            glist = os.listdir(ilist[i])
            
            print("ilist(before setList)")
            print(all([os.path.isdir(ilist[h]) or os.path.isfile(ilist[h]) for h in range(len(ilist))]))
            #ilistが全てファイルかディレクトリである事が分かる
            
            setList(ilist[i],glist)
                        
            print("ilist(after setList)")
            print(any([os.path.isdir(ilist[h]) or os.path.isfile(ilist[h]) for h in range(len(ilist))])) 
            #ilistが全てファイルでもディレクトリでもない事が分かる
            
            del ilist[i]
            ilist[i:i] = glist

        if os.path.isdir(ilist[i]):
            print(i)
            cntn.append(i)
            cnts.append(ilist[i])
            glist = os.listdir(ilist[i])
            
            setList(ilist[i],glist)
            
            del ilist[i]
            ilist[i:i] = glist

setList(a,flist)
print(flist)
print(cntn)
print(cnts)
os.chdir(a)

l = 0
for i in range(len(flist)):    
    if cntn:
        if i == cntn[l]:
            os.chdir(cnts[l])
            if l < len(cntn) - 1:
                l += 1
    num += os.path.getsize(flist[i])

print("number of file :" + str(len(flist)))
print("size of file   :" + str(num))
