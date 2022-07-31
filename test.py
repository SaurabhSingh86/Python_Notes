"""

2. Decorator with example and explain

3. {} - valid
    {()} - valid
    [})] - invalid
Stack operations
Check closing braces is equal to open braces and count of it

4.
Class employee
Takes - name, age, place
Class employer
Access it as employee and take employee method
Print methods
"""

""" WAP to reverse the string without using slicing """

# def reverse(string):
# 	string = "".join(reversed(string))
# 	return string
# my_number = "123456"
# print ("The given number is : ",end="")
# print (my_number)
# print ("Reversing the given number using reversed is : ",end="")
# print (reverse(my_number))


"""
# l = [1, 2, 3, 4, 5]
# a = 7
# #output = [3, 4]
# Add any 2 item in list l which gets sum=7 ...as output ie.,[3,4]
# """
#
# l = [1, 2, 3, 4, 5, 6]
# a = 7
# sum = 0
# for i in range(len(l)-1):
# 	if l[i] + l[i+1] == a:
# 		print(l[i], l[i+1])


""" Fetch which is the common character in the list 
In all the 4 strings g is common so have to fetch g """

l = ["glory ", "glass", " sight", "fight"]
w1, w2, w3, w4 = l
for char in w1:
    if char in w2 and char in w3 and char in w4:
        print(char)
