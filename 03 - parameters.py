# let's take a look at another function:

def hello(name):
    print("Hello","Peyton")

# What is the 'name' there? It doesn't have any quotation marks, and it's there twice.

# in the first line: def hello(name), the name is a parameter. A parameter is a variable which must be passed into the function externally.

# inside of the function: print("Hello",name), the name will reflect whatever was passed externally.

# Note that Python's print statement is pretty cool. You can send it multiple values separated by commas, and it will automatically put a space between them when outputting.

# How do we call this function?

# We must pass an argument to the function.

# An argument is the value that is sent to the function when you call it.

hello("P", "S")

# in this case, the argument is "Dan"

# Try running the script and see what is output.

# Change the name "Dan" to something else. It should still work.

# BREAK IT:
# What happens if you remove the name entirely and try to call hello() without anything inside?
# What happens if you put multiple arguments in, like hello("Dan","Sarah")?
# Why did the errors occur?

