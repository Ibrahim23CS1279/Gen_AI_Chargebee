# FUNCTIONS

def abc():
    print("hello world")
    print("123")

abc()


def add(a, b):
    print(a + b)

add(2, 3)


# OBJECT ORIENTED PROGRAMMING

class First:
    a = 78

    def method1(self):
        print("Method1")


# Create object
o1 = First()

print(o1.a)
o1.a = 80   # modifying value
print(o1.a)

o1.method1()


# INHERITANCE (Parent -> Child)

class Second(First):
    b = 45

    def method2(self):
        print("Method2")


s1 = Second()

print(s1.b)
print(s1.a)   # inherited from First
s1.method2()


# MODULES

# Different ways to import

# import cal
# cal.add(2,3)

# import cal as m
# m.sub(2,3)

# from cal import add
# add(4,5)

from cal import *

add(5, 4)
sub(5, 4)
mul(5, 4)
div(5, 4)