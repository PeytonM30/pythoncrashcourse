# go through existing tasks, listing each one, asking the user if they completed it
# If they completed it, remove it from the list, if not, keep it on the list

# ask the user to add more todos.
# Allow them to quit out when they are done adding their todos.

# make sure todos.txt exists
# read todos from todos.txt as a list of strings. Each line should have its own element in the list
try:
    with open("todo_list.txt", "r") as f:
        content = f.read()
        todo_list = content.split("\n")

except FileNotFoundError:
    with open("todo_list.txt", "w") as f:
        f.write("")

remaining_todo_list = []
for todo in todo_list:
        print(todo)
        user_input = input("Completed? (y/n)")
        if user_input != "y":
            remaining_todo_list.append(todo)

print(remaining_todo_list)

while True:
    new_todo = input("Add todo (q to quit): ")
    if new_todo == "q":
        break
    else:
        remaining_todo_list.append(new_todo)

with open("todo_list.txt", "w"):
    output = "\n".join(remaining_todo_list)
    f.write(output)
# for loop through the list
    # print the to-do
    #ask the user if they completed this
        # yes: remove it
    # else
        # no: keep it

# while loop
    # ask for another to-do
    # if they input "q", 
        # quit out with "break"          
    # else
        # add to to-do list

# write new to-dos to file