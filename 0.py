n = int(input())
ans=[]
for i in range(n):
    inp = input()
    a,b = map(int, inp.split())
    if a%b==0:
        ans.append(0)
    else:
        ans.append(b-a%b)

for i in ans:
    print(i)