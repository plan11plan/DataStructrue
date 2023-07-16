n, target = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

count = 0
for coin in arr:
    if target >= coin:
        quotient, target = divmod(target, coin)
        count += quotient
        if target == 0:
            break
print(count)
