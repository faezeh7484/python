def aval(number):
    count=0
    for x in range(1,number):
        if number%x==0:
            count+=1
    if count==1:        
        return 'aval'

javab=dict()
for i in range(0,10):
    adad=int(input())
    mlist=[]
    for b in range(1,adad+1):
        if adad%b==0:
            mlist.append(b)
            avalha=0

    for maghsum in mlist:        
        if aval(maghsum)=='aval': 
            avalha+=1
    #print(adad,avalha)
    javab[adad]=avalha

javabdic = {val[0] : val[1] for val in sorted(javab.items(), key = lambda x: (-x[1], -x[0]))}
a=list(javabdic.keys())
b=list(javabdic.values())
print('%s %s'%(a[0],b[0]))



  

        