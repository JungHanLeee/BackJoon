n,k=map(int,input().split())
arr=[]
resultarr=[]
for i in range(1,n+1):
   arr.append(i)
z=0
for i in range(n):
   z += k-1
   if z >= len(arr):
      z = z%len(arr)
   resultarr.append(str(arr[z]))
   del arr[z]

print("<",", ".join(resultarr)[:],">", sep='')

