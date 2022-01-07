e,s,m=map(int,input().split())
i=1
j=1
k=1
cnt=1
while(True):
    if(i==e and j==s and k==m):
        break
    i+=1; j+=1; k+=1; cnt+=1
    if i == 16:
        i = 1
    if j == 29:
        j = 1
    if k == 20:
        k = 1

print(cnt)

