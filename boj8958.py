n=int(input())
while(n>0):
    arr=list(input())
    cnt=0
    sum=0
    for i in range(len(arr)):
        if arr[i]=='O':
            cnt+=1
            sum = sum + cnt
        else:
            cnt=0
    print(sum)
    n-=1
