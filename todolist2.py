#Katie Siu, Mia Sanchez
#To Do Lists 2
#1/12


#Initialize
#Functions

todoList = ["milk", "eggs", "apples", "bananas", "strawberries", "butter", "cheese"]

while True:

    x = int(input("Choose a function: \n1. Add a task to the to-do list \n2. View the current to-do list \n3. Mark a task as completed \n4. Remove a task from the to-do list \n5. Remove all tasks from the to-do list \n6. Sort the list alphabetically \n7. Count the # of Items on the To-do List \n8. Exit the program \n"))

    if x == 1:
        item = input("What item would you like to add?")
        todoList.append(item)

    if x == 2 : 
        print(todoList)

    if x == 3:
        task = input("Which task is completed?")
        position = int(todoList.index(task))
        todoList[position] = task + " x"

    if x == 4:
        item = input("What item would you like to delete?")
        todoList.remove(item)
    
    if x == 5:
        todoList.clear()

    if x == 6:
        todoList.sort()

    if x == 7:
        todoList.len()

    if x == 8:
        break