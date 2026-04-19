"""
MULTI-LINE COMMENTING
Fundamental Data Types
int, float, string, complex, bool
"""

# Fundamental Data Types
a = 5
b = 1.1
c = "chargebee"
d = 4 + 2j
e = True

print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))


"""
Collection Data Types
list, tuple, set, dict
"""

# String Operations
a = "Jayapriya"

print(a)
print(a[0])     # J
print(a[4])     # p
print(a[-1])    # a
print(a[-3])    # i

# Slicing
print(a[4:8])   # priy

# Step slicing
print(a[::2])   # alternate characters
print(a[::-1])  # reverse

b = "Bavani Kandhan"

print(b[9:6:-1])    # naK
print(b[-5:-8:-1])  # naK
print(b[9:-8:-1])   # naK
print(b[-5:6:-1])   # naK

# Strip functions
b = "    Manideep Thalluru    "
print(b.strip())
print(b.lstrip())
print(b.rstrip())


# List (mutable)
a = ["usha", "manideep", "abirami"]
print(a)
print(type(a))

a[0] = "Baradwaj"
print(a)

# Tuple (immutable)
b = ("usha", "manideep", "abirami")
print(b)
print(type(b))
# b[0] = "Baradwaj"  # This will throw error

# Set (no duplicates)
c = {1, 1.1, "i"}
print(c)

# Dictionary
d = {1: "ravi", 2: "raj"}
print(d)
print(d[1])


"""
Nested Dictionary Example
"""

data = {
    "vegetables": {"carrot": 10, "tomato": 10, "onion": 10},
    "fruits": {"apple": 10, "orange": 29}
}

print(data)
print(data["vegetables"])


"""
Conditional Statements & Loops
Password Check System
"""

password = "admin@123"
limit = 0

while limit < 3:
    entry = input("Enter the password: ")

    if password == entry:
        print("Password match")
        break
    else:
        print("Check your password")
        limit += 1
else:
    print("Attempt limit reached")