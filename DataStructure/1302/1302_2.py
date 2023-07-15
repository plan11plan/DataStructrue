m = {}
output = ""
maxCount = 0
for _ in range(int(input())):
    text = input().strip()
    m[text] = m.get(text, 0) + 1  # use dict.get() to provide a default value if the key is not in the dictionary
    if m[text] > maxCount:
        maxCount = m[text]
        output = text
    elif m[text] == maxCount:
        if text < output:  # if the new text comes first alphabetically
            output = text

print(output)
