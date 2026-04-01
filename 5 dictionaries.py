# tuple
coords = (10, 20)

# Key properties:
"""
Ordered
Indexed
Immutable
Faster than lists
"""


# sets
numbers = {1, 2, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4}

# Key properties:
"""
Unordered
No duplicates
Very fast lookup
"""


# dictionaries
student = {
    "name": "Eklavya",
    "age": 21,
    "course": "Python"
}

student["age"] = 22
student["city"] = "Delhi"

# loop in dict
for key, value in student.items():
    print(key, value)
