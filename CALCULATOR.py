#firstly defining all operations
#addition of numbers
def add_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The addition of {first_num} and {second_num} is =",first_num+second_num)

#subtraction of numbers
def sub_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The subtraction of {first_num} and {second_num} is =",first_num-second_num)

#multiplication of numbers
def multiply_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The multiplication of {first_num} and {second_num} is =",first_num*second_num)

#division of nummbers
def div_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The division of {first_num} and {second_num} is =",first_num/second_num)

#floor division of numbers
def floordiv_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The floor division of {first_num} and {second_num} is =",first_num//second_num)

#remainder of numbers
def remainder_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The remainder of {first_num} to {second_num} is =",first_num%second_num)

#to the power of numbers
def power_num():
    first_num=int(input("Enter the first number of operation: "))
    second_num=int(input("Enter the second number of operation: "))
    print(f"The {first_num} to the power of {second_num} is =",first_num**second_num)

#main loop starts
while True:
    print("WELCOME TO THE WORLD OF CALCULATIONS ")

#printing the choices
    print("""
1] Addition(+)
2] Subtraction(-)
3] Multiplication(*)
4] Division(/)
5] Floor division(//)
6] Remainder(%)
7] First number to the power of second(**)
8] Exit
    """)
    print("Enter the number of operation or the Symbol of the operation to operate it on numbers:")
    choice=input()
    #operations selection by if else
    if(choice== "1" or choice=="+"):
        add_num()
    elif(choice== "2" or choice=="-"):
        sub_num()
    elif(choice== "3" or choice=="*"):
        multiply_num()
    elif(choice== "4" or choice=="/"):
        div_num()
    elif(choice== "5" or choice=="//"):
        floordiv_num()
    elif(choice== "6" or choice=="%"):
        remainder_num()
    elif(choice== "7" or choice=="**"):
        power_num()
    elif(choice== "8"):
        print("Thankyou for using the system \n GOODBYE")
        break
    else:
        print("The entered number is INVALID please try again with correct input \n ")


    