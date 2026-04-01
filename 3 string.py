# string

name = "eklavya"
print(name[0])   # a
print(name[3])   # a

print(name[-1])  # g
print(name[-3])  # v


# slicing

print(name[0:3])   # ekl
print(name[2:])    # lavya
print(name[:4])    # ekla


# methods
text = "hello world"

print(text.upper())      # "HELLO WORLD"
print(text.lower())      # "hello world"
print(text.title())      # "Hello World"
text.replace("world", "Python")  # "hello Python"








# list
fruits = ["apple", "banana", "mango"]

# indexing
print(fruits[0])   # apple
print(fruits[-1])  # mango

# slicing
nums = [10, 20, 30, 40, 50]

print(nums[1:4])  # [20, 30, 40]
print(nums[:3])   # [10, 20, 30]
print(nums[2:])   # [30, 40, 50]

total = sum(nums)
print(total)

# modifying

fruits[1] = "orange"
fruits.append("grapes")
fruits.insert(1, "kiwi")
fruits.remove("apple")
fruits.pop()        # removes last
fruits.pop(1)       # removes index 1


# looping through list
for fruit in fruits:
    print(fruit)



# nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
print(matrix[0][1])   # 2
