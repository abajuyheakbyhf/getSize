import os

num = 0
flist = []
cntn = []
cnts = []

a = input()
os.chdir(a)

flist = os.listdir(a)
#print(flist)

def setList(s,ilist):
    os.chdir(s)
    glist = []
    #print(ilist)
    for i in range(len(ilist)):
        #print(ilist[i])
        #print(i)
        if os.path.isdir(ilist[i]):
            #print(ilist[i])
            cntn.append(i)
            cnts.append(ilist[i])
            #print(ilist)
            glist = os.listdir(ilist[i])
            setList(ilist[i],glist)
            print(ilist[i])
            del ilist[i]
            #print(ilist)
            ilist.extend(glist)
            print(ilist[i])
            print(i)
            if os.path.isdir(ilist[i]):
                cntn.append(i)
                cnts.append(ilist[i])
                #print(ilist[i])
                glist = os.listdir(ilist[i])
                setList(ilist[i],glist)
                del ilist[i]
                #print(ilist)
                ilist.extend(glist)

setList(a,flist)
print(flist)
print(cntn)
print(cnts)
os.chdir(a)

for i in range(len(flist)):
    l = 0
    #os.chdir(a)
    #print(flist[i])
    if i == cntn[l]:
        os.chdir(cnts[l])
        l += 1
    num += os.path.getsize(flist[i])

#print(flist)
print("number of file :" + str(len(flist)))
print("size of file   :" + str(num))