import time
import os 

#initialization of the list to operate on
workspace=[]

#defining all tasks 
#adding
def add_task():
    intake_task=input("Enter the details of task to store :\n")
    if intake_task in workspace:
        print("This task already exists in the list")
    else:
        workspace.append(intake_task)
        print(f"The {intake_task} has been added ")
    
#def for displaying all tasks enrolled till now
def display_task():
    print("TO-DO-LIST : \n ")
    print(*workspace, sep = "\n")

#def for deleting the tasks not needed
def delete_task():
    give_deletion=input("Enter the task name to delete it from list \n ")
    if give_deletion in workspace:
        # del workspace[give_deletion]
        workspace.remove(give_deletion)
        print("Your work is done")
    else:
        print("Given data is not present in list please chek the correction again \n ")

# Asking user main loop
    
while True:
    print("WELCOME TO THE TO-DO-LIST SOFTWARE \n ")
    time.sleep(2)  #sleep for 2 sec for better experience
    print(""" 
    1) Add a task
    2) Display a task
    3) Delete a task
    4) Close
    """)
    #deciding their path by if else 
    choice=int(input("Enter the number according to your choice of operations \n"))
    if choice== 1:
        add_task()

    elif choice==2:
        display_task()

    elif choice==3 :
        delete_task()

    elif choice==4 :
        print("Thankyou for using the system \n")
        break

    else:
        print("The entered number is Invalid, Please try again with a Valid Number \n")





