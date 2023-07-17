n, v = map(int,input().split())
leaks = sorted(map(int, input().split()))

tape_length = v - 1
tape_count = 1
start = leaks[0]

for i in range(1, n):
    if leaks[i] - start <= tape_length:
        continue
    tape_count += 1
    start = leaks[i]

print(tape_count)
