arr=list(input())
cnt=0
zcnt=0
ocnt=0
for i in range(len(arr)):
    try:
        if arr[i]!=arr[i+1]:
            cnt+=1
    except IndexError:
        break
print((cnt+1)//2)