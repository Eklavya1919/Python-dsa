def n_times_name(n,name):
    if n==0:
        return
    else:
        n_times_name(n-1,name)
    print(name)

def print_till_n(n):
    if n==0:
        return
    else:
        print_till_n(n-1)
    print(n)

def print_till_one(n):
    if n==0:
        return
    else:
        print(n)
    print_till_one(n-1)

def sum_of_first_n(n):
    if n==0:
        return 0
    else:
        return n + sum_of_first_n(n-1)
    
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

def reverse_arr(nums):
    if len(nums)==0:
        return []
    else:
        return [nums[-1]] + reverse_arr(nums[:-1])

def is_palindrome(string):
    def reversed(string):
        if len(string)==0:
            return ""
        else:
            return string[-1] + reversed(string[:-1])
    return string==reversed(string)



