print("Lets create an exercise rutine.")

select = "Y"
while select == "Y" or select == "y":
    name=input("\nRutine Name: ")
    pre_work=int(input("Time to prepare: "))
    rest=int(input("Time to rest: "))
    print("\nLets create the work intervals for this rutine")
    
    while True:
        work=int(input("Time to work: "))
        detail=input("Description: ")
        add = input("Add more? Y/N ")
        if add == "Y" or add == "y":
            continue
        else:
            break
    print("\nYou stop adding intierval.")
    select=input("Do you want to add another rutine: Y/N ")
else:
    print("So we have: \nFor", name, "\nPreparation of: ", pre_work, "\n", work, "seg, of:", detail) 





