i = input()

k,n,w = map(int, i.split())

required = k*w*(w+1)//2

print(required - n)