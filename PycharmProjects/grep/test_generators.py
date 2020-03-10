# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)


def add():
    for index in range(-1, 20, 2):
        yield index

for i in add():
    print(i)



def rev_str(my_str):
    length = len(my_str)
    print(length)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)


def add(a, d):
    """
    index a * d   """
    return a * d

print(add.__doc__)
