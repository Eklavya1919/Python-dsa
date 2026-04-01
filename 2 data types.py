# conditionals

marks = 72

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")


# logical operator
# and    both true
# or     at least one true
# not    reverse

age = 25

if age > 18 and age < 60:
    print("Working age")
elif age < 18 or age > 60:
    print("Working age")


# loops

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1


# for loop
for i in range(5):
    print(i)


# break and continue

# break → stop the loop immediately
# continue → skip current iteration