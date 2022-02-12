# <<~~~~~~~~~~~~~~~~~ Local Variable ~~~~~~~~~~~~~~~~>>
# A variable which is created inside a function is called a lcoal variable.
# It can't be access outside the function.
# In order to modify a local variable in the global name space we need to use global keyword.


# Accessing a local variable

# def spam():
#     a = 20
#     print(a)                # => 20
#
#
# spam()
# print(a)                    # => Name Error


# to avoid this Name Error


def spam():
    global a
    a = 20
    print(a)                    # => 20


spam()
print(a)                        # => 20

