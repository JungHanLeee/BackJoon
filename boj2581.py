m=int(input())
n=int(input())
arr = []
for k in range(m, n+1):
    arr.append(k)
if m==1:
    arr.remove(1)
for i in range(m,n+1):
    for j in range(2,i):
        if i%j != 0:
            pass
        else:
            arr.remove(i)
            break
if(len(arr))==0:
    print("-1")
else:
    print(sum(arr))
    print(min(arr))
