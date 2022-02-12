# <<~~~~~~~~~~~~~~~~~ Non- Local Scope ~~~~~~~~~~~~~~~~>>
# Non-local-scopes are those which are neither local nor global.
# If a Nested function has to access & modify the variable of outer function, nonlocal keyword should be used.



def spam():
    a = 30
    def inner():
        nonlocal a
        a += 5          # => UnboundLocalError: (without using nonlocal keyword)
        print(a)
    inner()             # => 35
    print(a)            # => 35

spam()
print(a)                # => Name Error

