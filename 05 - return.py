# A function can also return something to whatever called it.

# For example:

def double("num"):
    return num * 2

# This function will take a number and return the number times 2 (doubling the number)

# Whatever is calling this function will use what is returned

num = 1

print("The number is:",num, "The number doubled is", double(num))

