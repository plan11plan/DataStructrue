for _ in range(int(input())):
    stk = []
    answer="YES"
    for ch in input():
        if(ch =='('):
            stk.append(ch)
        else:
            if(len(stk)>0):
              stk.pop()
            else:
                answer="NO"
                break
    if(len(stk)>0):
        answer="NO"
    print(answer)


