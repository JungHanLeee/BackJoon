import collections

arr=list(input().upper())
cnt=[0 for i in range(0,91)]

cnts=collections.Counter(arr)
for j in range(len(arr)):
    cnt[ord(arr[j])]+= 1

if len(arr)>1:
    if cnts.most_common(2)[0][1]==cnts.most_common(2)[1][1] :
        print("?")
    else:
        result = ord(cnts.most_common(1)[0][0])
        print(chr(result))
else:
    result=ord(arr[0])
    print(chr(result))
