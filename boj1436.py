n = int(input())
cnt = 0
i = 665

while True:
    i = str(i)
    if "666" in i:
        cnt += 1
        if cnt == n:
            break
    i = int(i) + 1

print(i)