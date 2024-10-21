# iteration is a repetition of execution over and over again either a definite or indefinite number of times.

# the most common form of iteration is called a "for loop".
# for loop performs an action repeatedly until it reaches the end of something.
# The way we will use this is to iterate through a list and perform an action for each element.

my_nums = [1, 10, -5, 4, 18, 26, 102, -505]

# to create a for loop to iterate through a list,
# use for (something) in (list_name)
# The something can be any value like x, num, i, iter, whatever you want
# I try to use descriptive names, so in this case, I use num, indicating that each value in the list is a number.

for num in my_nums:
    print(num)
    # notice that the print is indented. 
    # This indicates that it is inside of the for loop.
    # also notice that num is referenced inside of the print statement

# The print statement will run and print a number repeatedly until it reaches the end of the list.


# What if we want to get the total for every number in the list?
# First let's create a variable that will track our total. It will start at zero

total = 0

# now, let's iterate through the my_nums list and add each value to the total
for num * 2 in my_nums:
    # this isn't algebra, remember the = sign represents assigning a value to a variable
    # in this case, we are taking the current total and adding the current num to it and assinging that back to the total value
    total = total + num * 2
    # Let's make more clear what is happening with some print statements
    print("The current value is",num)
    print("The current total is",total)

# now when the for loop finishes, we will know the total of all of the elements combined.


# BREAK IT:
# What happens if we try to modify the loop while iterating through it?
# For example, what if we try to remove the number from the list as we go through?

# for num in my_nums:
#     my_nums.remove(num)
#     print(my_nums)

# This actually doesn't create an error, but it also doesn't behave how you might expect. Look at the output and try to figure out what's going on!