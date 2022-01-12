n=int(input())
while(n>0):
    r,s=input().split()
    r=int(r)
    s=list(s)
    p=[]
    for i in range(len(s)):
        for j in range(r):
            p.append(s[i])
    p="".join(p)
    print(p)
    n-=1