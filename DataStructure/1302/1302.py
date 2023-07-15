
m = {}
output = ""
maxCount = 1
for _ in range(int(input())):
    text = input().strip()
    if text in m:
        m[text] += 1
        if m[text] > maxCount:
             maxCount = m[text]
             output = text
        elif m[text] == maxCount:
            if (text < output):
                maxCount = m[text]
                output = text
    else:
        m[text] = 1
        if(maxCount==1):
            if(output):
              if (text < output):
                maxCount = m[text]
                output = text
            else:
                output=text
else:
    print(output)
