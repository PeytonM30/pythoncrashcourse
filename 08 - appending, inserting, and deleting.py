# Let's say we have a list, but we want to add more to it.
# we could even start with a blank list!

new_list = []

# Okay, so now we have an empty list. We can even verify it is empty by checking the length:
print("The length of the empty list is:",len(new_list))

# if I were to try calling the 0 index (new_list[0]), I would get an error, because it doesn't even have a 0 index.

# How can we add things to this list?
# lists in python have a built-in function called append()
# append adds an element to the end of a list.

new_list.append("Hello")
new_list.append("World")

print("New list version 2:", new_list)

# As a bonus, we can use another built in function insert() to sneak an element into another spot. For example, if we want to put something between "hello" and "world", we insert a new element at the index of 1, which will put a new element at index 1 and move everything else to the right.

new_list.insert(1, "to the")

print("New list version 3:", new_list)

# What if we want to delete something?
# Well, there is a built in delete function in python. This is actually a python function and not a list function, and you'll see the difference in the syntax:

del new_list[4]

# this deletes the 0th element of the list, leaving the rest the same

print("New list version 4:", new_list)

# Additionally, if we know the value of the element we want to delete, we can use list's remove function to remove by value


new_list.remove("World")
# NOTE: If there are multiple instances of the same value in the list, for example, if our list were ["Hello", "World", "World", "World"], remove would remove the first instance of the value and leave the rest remaining as ["Hello", "World","World"]

print("New list version 5:", new_list)


# BREAK IT:
# What happens if we try to del at an index that doesn't exist (an index too high)?
# What happens if we try to remove a value that doesn't exist in the list?
# Why do the errors occur?