from functools import singledispatch                        # work only first arguments


@singledispatch
def add(a, b):
    print("Base function add")


@add.register(int)
def _(a, b):
    print("Calling int")
    return a + b


@add.register(float)
def _(a, b):
    print("calling float")


@add.register(list)
def _(a, b):
    print("calling list")
    return sum(a + b)