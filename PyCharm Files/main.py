Sys_Username = "Vivan"
Sys_Password = "12345"

Attempt = 3

while True:
    UserName = input("Pls Enter your username here: ")
    UserPassword = input("Pls enter your password here: ")

    if UserName != Sys_Username and UserPassword == Sys_Password:
        print("Wrong Username Try Again ")
        Attempt -= 1

    elif UserName == Sys_Username and UserPassword != Sys_Password:
        print("Wrong Password Try Again ")
        Attempt -= 1
    elif UserName != Sys_Username and UserPassword != Sys_Password:
        print("Wrong Username And Password Try Again ")
        Attempt -= 1
    else:
        print("Logged-in-successfully")
        break

    if Attempt == 0:
        print("You no longer have access contact you system manager: ")
        break
