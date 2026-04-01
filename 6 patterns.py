x=5

# square
# x = int(input("Enter num: "))
# for i in range(1,x+1):
#     for j in range(1,x+1):
#         print("*", end="")
#     print()


# lower triangle
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()


# upper triangle
# for i in range(x):
#     for j in range(1,x-i+1):
#         print("*", end="")
#     print()


# lower triangle with nums
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# upper triangle with nums
# for i in range(x):
#     for j in range(1,x-i+1):
#         print(j,end="")
#     print()


# lower triangle with repeating numbers
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# pyramid
# for i in range(1, x + 1):
#     # print spaces
#     print(" " * (x - i), end="")
#     # print stars
#     print("*" * (2 * i - 1))


# reverse pyramid
# for i in range(x):
#     print(" "*i, end="")
#     print("*"*(2*(x-i)-1))


# 1/0 lower triangle
# for i in range(x):
#     for j in range(i+1):
#         if (i+j)%2==0:
#             print(1, end="")
#         else:
#             print(0, end="")
#     print()


# note
# n=5
# for i in range(1, n + 1):
#     # left side numbers
#     for j in range(1, i + 1):
#         print(j, end="")
    
#     # spaces
#     print(" " * (2 * (n - i)), end="")
    
#     # right side numbers (reverse)
#     for j in range(i, 0, -1):
#         print(j, end="")
    
#     print()

# lower triangle of pyramids
# c=1
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print(c, end=" ")
#         c+=1
#     print()


# lower triangle of capital letters
# for i in range(1,x+1):
#     for j in range(1, i+1):
#         print(chr(64+j), end="")
#     print()

# lower triangle of small letters
# for i in range(1,x+1):
#     for j in range(1, i+1):
#         print(chr(96+j), end="")
#     print()


# square borders
# for i in range(1,x+1):
#     for j in range(1,x+1):
#         if i==1 or j==x or i==x or j==1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# spiral
# for i in range(1, 2*x):
#     for j in range(1, 2*x):
#         if i == 1 or i == 2*x-1 or j == 1 or j == 2*x-1:
#             print(x, end=" ")
#         elif i == 2 or i == 2*x-2 or j == 2 or j == 2*x-2:
#             print(x-1, end=" ")
#         elif i == 3 or i == 2*x-3 or j == 3 or j == 2*x-3:
#             print(x-2, end=" ")
#         elif i == 4 or i == 2*x-4 or j == 4 or j == 2*x-4:
#             print(x-3, end=" ")
#         else:
#             print(1, end=" ")
#     print()
