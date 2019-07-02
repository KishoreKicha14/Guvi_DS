n=[int(s) for s in input().split()]
r=[]
r.append(n[1])
top=0
for i in range(n[0]):
    m=input().split()
    if(m[0]=='F'):
        r.append(m[1])
    else:
        r.append(r[top-1])
    top=top+1
print(r[top])   
