# let's start with the same number list
my_nums = [1, 10, -5, 4, 18, 26, 102, -505]

# What if we want the index along with the number? For example, maybe we want to print: 0 -> 1, 1 -> 10, 2 -> -5 and so on?

# First we get the length of our list. You remember how to do that right?
# len(my_nums)
# in our case, the length is 8
# now, from the length, we can create a range, using the range() function
# range takes an integer value (in our case 8), and creates something similar to a list, starting from 0, increasing by 1 and increasing until it is 8 elements long.
# So, the range(8) would be [0,1,2,3,4,5,6,7]
# We can actually convert a range into a list with list(range(8)), which you'll see in conditionals

# But how do we access the value from the list? For each of those numbers, we can call the list at that index
# For example, nums[0], which is 1, nums[1] which is 10, and so on.

# Putting it all together, we have a crazy nested function: range(len(my_nums))
# essentially meaning, we are getting a range from the length of the list my_nums
del my_nums
# this is the way we iterate if we also need the indices of the elements of the list:
for i in range(len(my_nums)):
    # generally when we iterate by index, we use "i" as the variable.
    print(i,"->",my_nums[i])
    # my_nums[i] uses the index to grab the element from the list

# unlike the last problem, because we are not iterating through the list directly, it is safe to make modifications to the list as we go through:




# BREAK IT: What happens if we try to delete everything from my nums using del by the index while iterating through?
# for i in range(len(my_nums)):
#     del my_nums[i]
#     print(my_nums)

# in this case, we do get an error. What causes the error?