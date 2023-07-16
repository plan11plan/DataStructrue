import itertools

n,target = map(int,input().split())

arr=[]
for _ in range(0,n):
    arr.append(int(input()))
arr.sort(reverse=True)

box=target
count=0
for value in arr:
    if(target<value):
        continue
    elif(target>value):
        while(box>0):
            if(box-value<0):
                break
            box = box - value
            count+=1
    else:
        count=1
        break

print(count)




