def count_digits():
    num = int(input("Enter num: "))
    if num==0:
        print(1)
    else:
        count = 0
        while num>0:
            count+=1
            num = num//10
        print(count)

def reverse_num(num):
    reversed = 0
    while num>0:
        reversed = reversed*10 + num%10
        num = num//10
    return reversed

def pali_num(num):
    reversed = reverse_num(num)
    return num==reverse_num

def gcd_nums(a,b):
    while b>0:
        a,b = b, a%b
    return a

def armstrong_num(num):
    digits = len(str(num))
    sum = 0
    for i in str(num):
        sum += int(i)**digits
    return sum==num

def all_divisors(num):
    res = []
    for i in range(1,num//2):
        if i*i>num:
            res.sort()
            return res
        elif i*i==num:
            res.append(i)
            res.sort()
            return res
        else:
            if num%i==0:
                res.append(i)
                res.append(int(num/i))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(13))