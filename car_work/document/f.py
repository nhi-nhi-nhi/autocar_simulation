n = list(input())
i=0

while i < len(n):
    if n[i]=='=':
        n = n[:i+1] + n[i:]
        i += 1
    i += 1
    
for i in n:
    print(i, end='')