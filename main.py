from pyad import *

pyad.set_defaults(server="geek.local", user="Administrator", password="BS14Lf3")
#user = pyad.aduser.ADUser.from_cn("Administrator")

print("Welcome to the geek.local Active directory."
      "What do you want to do? You can answer with number: ")
op = True
while op:
    print("\n1. Make a new user\n"
          "2. Delete a user \n"
          "3. Change a department from user \n"
          "4. Give a user user more permission\n"
          "5. Add a user to a group\n"
          "6. Delete a user from a grope\n"
          "0. Exit")
    user_input = int(input(""))


    if user_input == 0:
        op = False
    else:
        if user_input == 1:
            print("Make a new user for: \n"
                  "1. Einkauf department \n"
                  "2. Finanzen department \n"
                  "3. Geschäftsführung department \n"
                  "4. IT department \n"
                  "5. Lager department \n"
                  "6. Personal department \n"
                  "7. Verkauf department \n"
                  "8. Verwaltung department")
            user_input = int(input(""))

            if user_input == 1:
                name = input("Please write the user name: ")
                password = input("Please write the user password: ")

                ou = pyad.adcontainer.ADContainer.from_dn("OU=Ben_Einkauf,OU=Benutzer,OU=GEEK-Fitness,DC=geek,DC=local")
                new_User = pyad.aduser.ADUser.create(name, ou, password=password, upn_suffix=None, enable=True)

                user = pyad.aduser.ADUser.from_cn(name)
                group = pyad.adgroup.ADGroup.from_cn("Grp_Einkauf")
                group.add_members([user])


            elif user_input == 2:
                name = input("Please write the user name: ")
                password = input("Please write the user password: ")

                ou = pyad.adcontainer.ADContainer.from_dn("OU=Ben_Finanzen,OU=Benutzer,OU=GEEK-Fitness,DC=geek,DC=local")
                new_User = pyad.aduser.ADUser.create(name, ou, password=password, upn_suffix=None, enable=True)

                user = pyad.aduser.ADUser.from_cn(name)
                group = pyad.adgroup.ADGroup.from_cn("Grp_Finanzen")
                group.add_members([user])

        elif user_input == 2:
            name = input("Please write the user name: ")
            user = pyad.aduser.ADUser.from_cn(name).delete()

        elif user_input == 6:
            name = input("Please write the user name: ")
            user = pyad.aduser.ADUser.from_cn(name)
            group_name = int(input("From which Group is the user: \n"
                               "1. Einkauf\n"
                               "2. Finanzen\n"
                               "3. Geschäftsführung\n"
                               "4. IT\n"
                               "5. Lager\n"
                               "6. Personal\n"
                               "7. Verkauf\n"
                               "8. Verwaltung\n"
                               ""))
            if group_name == 1:
                group = pyad.adgroup.ADGroup.from_cn("Grp_Einkauf")
                group.remove_members([user])

            elif group_name == 2:
                group = pyad.adgroup.ADGroup.from_cn("Grp_Finanzen")
                group.remove_members([user])




