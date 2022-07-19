# ---------------------------- __name__ ------------------------------------

# Every python program contain, a special variable __name__ which is added internally.
# __name__ helps us to know whether the program is executed as an individual program or as a module.
# If the program executed as a individual program then the value of this variable is “__main__”
# If the program executed as a module from some other program then the value of this variable is the name of module
# where it is defined


# Example:
# if __name__ == "__main__":
#     print("direct execution of program")
# else:
#     print("program is executing indirectly")
#
# # output = direct execution of program


# the main use of this special variable is
# Step 1

# def m1():
#     print("We are executing m1 function")
#
#
# def m2():
#     print("We are executing m2 function")
#
#
# def m3():
#     print("We are executing m3 function")
#
# m1()
# m2()
# m3()

# We are executing m1 function
# We are executing m2 function
# We are executing m3 function

# Step 2


def m1():
    print("We are executing m1 function")


def m2():
    print("We are executing m2 function")


def m3():
    print("We are executing m3 function")


if __name__ == "__main__":
    m1()
    m2()
    m3()

# We are executing m2 function