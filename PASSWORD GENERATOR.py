import random
import string

# simple contains all alphabets
def simple_pass():
    length=int(input("Enter the length of Password :"))
    print("Your password is : ",end="")

    for i in range(length):
        # randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        # print(randomLowerLetter,end="")
        print(randomUpperLetter,end="")

# moderate contains all the numbers
def Moderate_pass():
    length=int(input("Enter the length of Password :"))
    print("Your password is : ",end="")

    for i in range(length):
        print(random.randint(1, 9),end="")

# High contains combination of alphabets & numbers
def High_pass():
    length=int(input("Enter the length of Password :"))

    characters = string.ascii_letters + string.digits

    #joining all the outputs
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Your password is : ",password)

# Complex contains combination of alphabets,numbers & punctuation(spl.charac)
def generate_complex_password():
    length = int(input("Enter the length of Password: "))

    combination = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

    #checking the validity of length of password
    if length < 8:
        print("For complex password length should be minimum 8")
    else:
        # Generate the password
        password_list = random.sample(combination, length)
        password_str = ''.join(password_list)
        print("Your password is: ", password_str)

#first interface for asking
print("""
1] Simple level Password
2] Moderate level Password
3] High level password
4] Complex level Password (minimum length should be 8)
""")

# repeated loop
while True:
    user_input=input("\nEnter the number of the above mentioned levels of complexity (or enter exit to end program): ")

    #If Else calling function
    if(user_input=="1"):
        simple_pass()

    elif(user_input=="2"):
        Moderate_pass()

    elif(user_input=="3"):
        High_pass()

    elif(user_input=="4"):
        generate_complex_password()

    elif(user_input=="exit"):
        break

    else:
        print("Enter the correct input, Try Again")
    

