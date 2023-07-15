from itertools import combinations

arr = []
for _ in range(0,9):
    arr.append(int(input()))

for i in combinations(arr, 7):
    if(sum(i)==100):
       l = list(i)
       l.sort()
       for i in range(0,len(l)):
           print(l[i])
       break
