import heapq
import sys

pq=[]
for _ in range(int(sys.stdin.readline())):
    x =int(int(sys.stdin.readline()))
    if(len(pq)==0 and x ==0):
        print(0)
        continue
    if(x!=0):
        if(x>0):
            heapq.heappush(pq,(x,x))
        elif(x<0):
            heapq.heappush(pq,(-x,x))
    elif(x==0):
        absolute, number = heapq.heappop(pq)
        print(number)


