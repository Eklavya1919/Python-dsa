c=0
def cou(num):
    if num==0:
        return 
    cou(num//10)
    c+=1

cou(154)
print(c)

