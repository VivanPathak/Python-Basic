Username = input("Pls enter your username: ")
Username_edit = Username.replace(" ","")
Company_Name =  input("Pls enter the compony name:")
Compony_edit = Company_Name.replace(" ","")
Gmail= Username_edit + "." + Compony_edit +"@gmail.com"
Gmail_edit = Gmail.lower()
Password = Compony_edit + "#123"
print("Gmail: ", Gmail_edit, "Password: ", Password)