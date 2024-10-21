# There are different types of data in Python (or any programming language)
# Each type can have different operations performed on it.

# For this assignment, we only need to focus on two important data types:
# integers and strings

# An Integer is a whole-number numerical value (positive or negative)

num1 = 20
num2 = -5
num3 = 8
num4 = num1 + num2 * num3

# okay, so what is the value of num4? I hope you remembered your orders of operations from math class! Please excuse my dear Aunt Sally.
print("The value of num3 is:",num4)

# integers are cool because we can do several operators:
print(num1,"+",num3,"=",num1+num0)
print(num1,"-",num3,"=",num1-num3)
print(num1,"*",num3,"=",num1*num3)
print(num1,"/",num3,"=",num1/num3) 
# when you divide, the result will change to a floating point number instead of an integer.
# We don't need to learn about floating point numbers at this time, but it may be helpful in the future.
print(num1,"%",num3,"=",num1%num3)
# NOTE: The % is called a "modulo" or "mod". It will give you the remainder of a division as an integer
# For example, 19%5 is 4, because 19 / 5 is 3 with a remainder of 4. 

# A string is a series of characters. The characters can be letters (capital or lowercase), numbers, spaces, punctuation, or even a lot of symbols. There is even support for foreign language characters.

# strings can be surrounded by a single apostrophe ' or a quotation mark ". Having this flexibility can be helpful, incase we want quotations or apostrophes within the string.

string1 = "This is Dan's"
string2 = " homework."
string3 = ' According to Dan. This is "clever."'
string4 = string1 + string2 + string3

# you can see for string 3, I used ' instead because I wanted to put " inside the string. There are other ways to handle that as well, but we don't need to get into that today.

# Okay, but what happens when we add them together?

print("The value of string4 is:", string4)

# if you run the assignment, you'll see the answers for both num3 and num4

# What happens if we multiply a string by an integer?
# for example:
# print("Hello " * 10)
# try it out! It actually works!


# BREAK IT:
# What happens if you try to subtract a string from a string?
# What happens if you multiply a string by a string?
# What happens if you divide an integer by zero?
# Why do these errors occur?