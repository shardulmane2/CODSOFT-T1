

name = input("Please enter your name: ")
print(f"Welcome {name} to the TO-DO application :)\n")

ns = int(input("How many tasks have you planned for today? "))
np = int(input("How many have you completed today? "))


nw = ns - np

if nw > 0:
    print(f"\nYou have {nw} tasks left to complete!!")
    print("Get to Work!!")
    print("\nPlease list the tasks:")
    tasks = []
    for l in range(1, nw + 1):
        task = input(f"T{l}: ")
        if task.lower() == "done":
            break
        tasks.append(task)

    print("\nList of your tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")



def tq():
    print(f"Thank you {name},for using the TO-DO Application :)")


def use():
    print("\n What do you want to do with the list?")
    print("1. Delete\n2. Replace\n3. Update completed tasks\n4. Exit")
    op = input("Please select a choice: ")


print("\n What do you want to do with the list?")
print("1. Delete\n2. Replace\n3. Add a new task\n4. Update completed tasks\n5. Exit")
op = input("Please select a choice: ")

if op == "1":
    print("\nWhat do you want to delete?\n")
    print("1. Element from the list \n2. The entire list \n3. Exit")
    ki = input("Please enter a number: ")
    if ki=="1":
        oi=input(str("What element would you like to remove?"))
        tasks.remove(oi)
        print(f"The list has now removed {oi} and now looks like:\n {tasks}")
        a=input(str("Anything else?")).lower()
        if a=="yes":
            use()
            if a=="no":
                tq()
        if ki == "2":
            tasks.clear()
            print("The list is empty!!")
            j=input(str("Anything else?")).lower()
        if j=="yes":
            use()
        if j=="no":
            tq()


        if ki=="3":
            tq()

def ez():
    sel = input("Which element do you want to replace(name)? ")
    if sel in tasks:
        todel = tasks.index(sel)
        tasks.pop(todel)
        new = input("Input the task you want to add in the updated list:")
        tasks.insert(todel, new)
    while sel not in tasks:
        print(f"The task {sel} does exist in the list!!")
        print("Please enter a valid choice!!")
        break


if op == "2":
    sel = input("Which element do you want to replace(name)? ")
    if sel in tasks:
        todel = tasks.index(sel)
        tasks.pop(todel)
        new = input("Input the task you want to add in the updated list:")
        tasks.insert(todel, new)
    else :
        print(f"The task {sel} does exist in the list!!")
        print("Please enter a valid choice!!")
        ez()

        o=input(str("Anything else?\n")).lower()
        if o=="yes":
            use()
        if o=="no":
            tq()



if op=="3":
    print("Seems like you missed a task!!")
    p=input(str("Which task have you forgotten to add to the list: "))
    ind=int(input("Where do you wish to insert the task:"))
    k=ind-1
    tasks.insert(k,p)
    print(f"This is the new list after adding the {p} task:\n {tasks}\n")
    q=input(str("Anything else?\n")).lower()
    if q=="yes":
     use()
    if q=="no":
        tq()



    comp = []
if op=="4":
    u=int(input("How many tasks have you completed?"))
    for i in range(u):
        while j in tasks:
            try:
                j = input(str("Which tasks have you completed?(name)"))
                break
            except ValueError:
                print("Invalid choice !!")
        if j in tasks:
            tasks.pop(j)
            comp.insert(j)
            print(f"This is the task that is completed:\n{comp}")

if op=="5":
    tq()

if op >"5":
    print(f"{name} please enter a valid number!!")


if nw == 0:
        print("You have completed all your tasks for today! Good luck for tomorrow!!")
if nw < 0:
        print("You have entered wrong information. Please check the information and try again!!")



