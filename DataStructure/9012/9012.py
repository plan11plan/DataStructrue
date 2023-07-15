for _ in range(int(input())):
    answer = ""
    count = 0
    for ch in input():
        if(ch == '('):
            count+=1
        elif(ch ==')'):
            count-=1

        if(count<0):
            answer = "NO"
            break
        elif(count>0):
            answer = "NO"
        else:
            answer = "YES"
    print(answer)