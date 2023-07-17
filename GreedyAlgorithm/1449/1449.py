n,v = map(int,input().split())

arr = list(map(int, input().split()))
arr.sort()

tapeCm  =v-1
count =0
start =arr[0]
flag =False
if(v!=1):
 for i in range(1,n):
    if(flag == True):
        start=arr[i]
        flag=False
        if(i==n-1):
            count+=1
        continue

    lenth=arr[i]-start
    if(tapeCm>lenth):
        if(i==n-1):
            count+=1
        continue
    elif(tapeCm ==lenth):
            count+=1
            flag =True
    elif (tapeCm < lenth):
        if(i==n-1):
            count+=2
            continue
        count += 1
        start = arr[i]
else:
    count=n


print(count)

