# Triangle Pattern : =>
# -------------------------------------------------------------------------------------------------------------------

# Left Justified Triangle
# for i in range(1, 6):
#     print(f"{'* '*i:<5}")

"""
*
* *
* * *
* * * *
* * * * *
"""


# Right Justified Triangle
# for i in range(1, 6):
#     print(f"{' *'*i:>10}")

"""
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

# Equilateral Triangle
# for i in range(1, 6):
#     print(f"{'* ' * i : ^10}")

"""
    *     
   * *    
  * * *   
 * * * *  
* * * * * 
"""

# for i in range(1, 6):
#     print(f"{' *' * i : ^10}")

"""
*    
    * *   
   * * *  
  * * * * 
 * * * * *
"""


# Inverted Triangles (Left Justified)
# for i in range(6, 0, -1):
#     print(f"{'* ' * i: <6}")
"""
* * * * * * 
* * * * * 
* * * * 
* * * 
* *   
*   
"""

# Inverted Triangles (Right Justified)
# for i in range(6, 0, -1):
#     print(f"{'* '*i:>12}")
"""
* * * * * * 
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
"""


# Inverted Triangles (Centre)
# for i in range(6, 0, -1):
#     print(f"{'* '*i:^12}")

"""
 * * * * * *
  * * * * * 
   * * * *  
    * * *   
     * *    
      * 
"""


# Number Pattern in triangle: =>
# ------------------------------------------------------------------------------------------------------------------

# Left Justified

# class Solution:
#     def
# pat = ''
# for i in range(1, 6):
#     pat += str(i) + " "
#     print(f'{pat:<5}')



"""
1    
1 2  
1 2 3 
1 2 3 4 
1 2 3 4 5 
"""

# Number Pattern in triangle (Right Justified)
# pat = ''
# for i in range(1, 6):
#     pat += str(i) + " "
#     print(f'{pat:>10}')

# for loop

count = 1
temp = ""
while count < 5:
    temp += str(count) + " "
    print(temp)
    count += 1

"""
        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5

"""
# Number Pattern in triangle (Centre)
# pat = ''
# for i in range(1, 6):
#     pat = pat + ' ' + str(i)
#     print(f'{pat:^10}')

"""
     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5

"""


# Alphabet Pattern
# ------------------------------------------------------------------------------------------------------------------

# Left justification
# pat = ""
# for i in range(ord("a"), ord('d') + 1):
#     pat += chr(i) + " "
#     print(pat)

"""
a 
a b 
a b c 
a b c d 
"""

# Right Justification
# pat = ""
# for i in range(ord("a"), ord("d") + 1):
#     pat += chr(i) + " "
#     print(f'{pat:>8}')

"""
      a 
    a b 
  a b c 
a b c d  
"""

# Central
# pat = ""
# for i in range(ord("a"), ord("d") + 1):
#     pat += chr(i) + " "
#     print(f'{pat:^8}')

"""
   a    
  a b   
 a b c  
a b c d 
"""


""" WAP to print the following pattern 
* 
* 
* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * * 

"""

# for num in range(1, 11):
#     if num % 2 == 0:
#         r = num / 2
#         print("* " * int(r))
#
#     else:
#         print("* ")


""" Write a program to get the below output """
"""
* 
* * 
* 
* * * 
* 
* * * * 
* 
* * * * * 
"""

# for i in range(1, 5):
#     print("* " * 1)
#     print("* " * (i+1))


"""
1 
2 3 
4 5 6 
7 8 9 10 
"""

# Method 1:
# num = 1
# for x in range(1, 5):
#     for y in range(1, x + 1):
#         print(str(num) + " ", end="")
#         num += 1
#     print()



