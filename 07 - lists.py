# A list is Python's version of other programming languages "arrays"
# Python lists are similar to arrays, with a few key differences.
# However, the differences are a bit to complicated to get into in this lesson.
# If you've used arrays in other languages, you may notice the differences though.

# a list is wrapped in brackets. It contains a series of data.
# the data can be strings, integers, or pretty much any other data type.
my_list = ["Hello", "World", "My", "Name","is","Dan"]

# how many elements are in the list? To find out, we can print the length of the list using a built-in function len()
print("The length of the list is", len(my_list))


# printing the list itself will show the entire list separated by commas
print("My list:", my_list)

# The length of the list is 6, indicating there are six elements in the list:
# 0 "Hello"
# 1 "World"
# 2 "My"
# 3 "Name"
# 4 "is"
# 5 "Dan"

# Wait a minute! Who the heck starts counting from zero instead of one?
# In programming, the first element of a list or an array, is indexed at 0, the second at 1, and so on.
# I know, I know. I didn't make the rules, I just explain them.

# So, if I want to print "Name" from the array, I need to call the 4th element, which is actually at index 3.

# to call index 3 of my_list, use brackets in front of the name of the list

print("Index 3 of my_list is:",my_list[8])

# What happens if we try to go negative with the index?
# Try printing my_list[-1]

# print(my_list[-1])

# Wow! It actually works! you can count backwards through a list using negative numbers.

# We can also sort lists using the sort(). If we sort a list of integers, it will sort them in numerical order. What happens if we sort a list of strings?

my_list.sort()

print(my_list)

# Well, it looks like it sorted it in alphabetical order, but what the heck is going on with 'is' at the end?
# Strings are made up of characters and each character is associated with an ordinal number. 
# The capital letters actually come befor lower case letters in the ordinal character list (A-Z is 65-90, and a-z is 97-122)
# So, when sorted, the capital letters come before lower case letters. 


# BREAK IT
# what happens if you try a number that is higher than the highest index of 5?
# Why do you get the error?
