""" 1. Check whether the user given number is factorial or not using recursion """

""" 2. Write a recursion program to find the fibonacci series until the given range. """
n = 20

""" 3. WARP to print the reverse of string values in the list """
l = [1, "hello", "bye", 2, "thanks"]

def reverse_(sequence, l1=[]):
    if sequence:
        if isinstance(sequence[0], str):
            l1.append(sequence[0][::-1])
            return reverse_(sequence[1:], l1)
    return l1


list_ = [1, "hello", "bye", 2, "thanks"]
print(reverse_(list_))


""" WARP that prints the number 10, ten times """

""" WARP to find the sum first n numbers """

