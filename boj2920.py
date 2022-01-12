input_arr=input()
input_arr=input_arr.replace(' ','')
ascending=sorted(input_arr)
desending=sorted(input_arr,reverse=True)
for i in range(1):
    ascending="".join(ascending)
    desending="".join(desending)

if input_arr==ascending:
    print("ascending")
elif input_arr==desending:
    print("descending")
else:
    print("mixed")