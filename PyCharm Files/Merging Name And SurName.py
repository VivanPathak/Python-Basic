Name    = ["Vivan", "Aadi","Aviral", "Arinjay","Rishabh","Mihir", "Aksh"]
Surname = ["Pathak","Chouksey","Kaurav","Mourya","Singh","Shahani","Bhaskar"]

Famous = list(zip(Name,Surname))
Famous.sort()
for Name, Surname in Famous:
    print(Name,Surname)
    