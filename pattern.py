# Left Justified Triangle
"""
*
* *
* * *
* * * *
"""

# # Method 1
# for row in range(4):
#     for col in range(row + 1):
#         print("*", end=" ")
#     print()
#
#
# # Method 2
# for row in range(1, 5):
#     print('* ' * row)


# Right Justified Triangle
"""
        * 
      * * 
    * * * 
  * * * *  
"""

# Method 1
for row in range(1, 5):
    print(f'{"* " * row:>8}')
