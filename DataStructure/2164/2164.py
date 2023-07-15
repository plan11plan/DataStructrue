from collections import deque

n= int(input())
q = deque()
count =1
for i in range(n):
    q.append(i+1)
while(len(q)!=1):
    if(count ==1):
        q.popleft()
        count=0
    else:
         ch= q.popleft()
         q.append(ch)
         count=1
a = q.pop()
print(a)