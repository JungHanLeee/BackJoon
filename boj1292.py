a,b=map(int,input().split())
sum=0
arr=[]
arr.append(0)
for i in range(1000):
    for j in range(i):
        arr.append(i)
for i in range(a,b+1):
    sum+=arr[i]

print(sum)
