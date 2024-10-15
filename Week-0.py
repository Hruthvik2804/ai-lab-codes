# Write a program to demonstrate different number data types in Python.
def n1():
    x = 1
    y = 2.0
    print("Integer:", x)
    print("Float:", y)
    
# Write a program to create, append, and remove lists in python.
def n2():
    print("Creating List")
    l = []
    print("Empty list:", l)
    i = 0
    while i < 2:
        val = int(input("Enter value to append in list: "))
        l.append(val)
        i += 1
    print("Appended list:", l)
    d = int(input("Enter value to remove: "))
    l.remove(d)
    print("Modified list:", l)

# Write a program to demonstrate working with tuples in python.
def n3():
    print("Creating Tuple")
    t = tuple()
    print("Empty tuple:", t)
    i = 0
    while i < 2:
        val = int(input("Enter value to append in tuple: "))
        t += (val,)
        i += 1
    print("Modified tuple:", t)
    print("Unpacking tuple of length 2")
    a, b = t
    print("a =", a)
    print("b =", b)

# Write a program to demonstrate working with dictionaries in python.
def n4():
    print("Creating dictionary")
    d = {}
    print("Empty dictionary:", d)
    i = 0
    while i < 4:
        val = int(input("Enter value to append in dictionary: "))
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
        i += 1
    print("Modified dictionary:", d)
    print("Dictionary keys:", list(d.keys()))
    print("Dictionary values:", list(d.values()))

def n5():
    l = []
    for i in range(3):
        x = int(input("Enter number: "))
        l.append(x)
    print("Maximum value is:", max(l))

if __name__ == "__main__":
    print("Question 1")
    n1()
    print()
    print("Question 2")
    n2()
    print()
    print("Question 3")
    n3()
    print()
    print("Question 4")
    n4()
    print()
    print("Question 5")
    n5()

