n=[]
while(n!=0):
    n = input()

    if n=='0':
        exit(0)
    else:
        revsen="".join(list(reversed(n)))
        if n==revsen:
            print("yes")
        else:
            print("no")