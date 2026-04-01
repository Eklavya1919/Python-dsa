# function
def greet(x):
    print("hello", x)

greet("eklavya")


# return function
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8


# default parameter
def greet(name="Guest"):
    print("Hello", name)

greet()          # Hello Guest
greet("Eklavya") # Hello Eklavya



# keyword argument

def profile(name, age):
    print(name, age)

profile(age=21, name="Eklavya")

