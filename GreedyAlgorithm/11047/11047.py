n,target = map(int,input().split())

arr= [int(input()) for _ in range(n)]
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




