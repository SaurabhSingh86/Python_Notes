# <<~~~~~~~~~~~~~~~~~ Global Variable ~~~~~~~~~~~~~~~~>>
# A variable which is created in global namespace i.e. outside of function
# It can only access inside a function but can't modify.
# In order to modify a global variable inside a function then we need to use global keyword.


# Accessing a global variable

# a = 10
#
#
# def spam():
#     print(a)                # => 10
#
#
# spam()
# print(a)                    # => 10


# Modify global variable
b = 10


def spam():
    global b
    b += 5
    print(b)                # => 15


spam()
print(b)                    # => 10

# => UnboundLocalError: local variable 'b' referenced before assignment