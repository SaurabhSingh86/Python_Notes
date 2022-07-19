# e.g. 1
# import special_variable
# print()
#
# # program is executing indirectly

# Step 1
# import special_variable
# special_variable.m2()

# We are executing m1 function
# We are executing m2 function
# We are executing m3 function
# We are executing m2 function

# the above output is not required to avoid this we have to use __name__ == "__main__"
# Step 2
import special_variable
special_variable.m2()