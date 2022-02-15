Your_username = "Vivan Pathak"
Your_password =  "Hello_2222"

Username = input("Pls enter your username: ")
Password = input("Pls enter your password: ")

if Username != Your_username and Password == Your_password:
 print("Wrong Username Try Again ")

elif Username == Your_username and Password != Your_password:
    print("Wrong Password Try Again ")

elif Username != Your_username and Password != Your_password:
    print("Wrong Username And Password Try Again ")

else:
    print("Logged-in-successfully ")





