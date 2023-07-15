d = dict()
for _ in range(int(input())):
    book = input()
    if book in d:
        d[book]+=1 # 처음 갯수 설정은 어디감?
    else:
        d[book]=1

m = max(d.values())
candi =[]
for k,v in d.items():
    if(v == m):
        candi.append(k)

candi.sort()
print(candi[0])