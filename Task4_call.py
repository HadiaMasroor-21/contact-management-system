contacts ={}

def add_contacts():
    print("----ADD NEW CONTACT----")
    name  = str(input("Enter YOUR Name : "))
    phone = int(input("Enter Your Phone Number : "))
    Email = (input("Enter Your Email : "))
    contacts[name] = {"Phone Number ": phone, "Email" : Email}
    print(f" NAME : {name} \n PHONE NO. : {phone} \n Email : {Email} \n added successfully in contact list")


def update_contacts():
    print("----Update Contacts----")
    name = input("Enter the name  you want to update : ")                                                                 
    if name in contacts :
      print("Enter the detail that you want t change : ")
      name  = str(input("Enter New Name : "))
      phone = int(input("Enter the Phone Number : "))
      Email = (input("Enter the Email : "))
      contacts[name] = {"Phone Number ": phone, "Email" : Email}
      print(f" NAME : {name} \n PHONE NO. : {phone} \n Email : {Email} \n added successfully in contact list")   
    else:
       print("contact not found")

def delete_contacts():
   print("---------Delete Contacts-----")
   name = input("Enter the name you want to delete : ")
   if name in contacts:
      del contacts[name]
      print("Contact deleted")
   else:
      print("Contact not found!")


while True:
   print("---Call Log Menu ----")
   print("1. Add Contacts")
   print("2 Update Contacts")
   print("3. Delete Contacts")
   print("4. Exit")

   choice = input("Enter Your Choice : ")
   if choice == "1":
      add_contacts()
   elif choice == "2":
      update_contacts()
   elif choice == "3" :
      delete_contacts()
   elif choice == "4" :
      print("Exiting.... Goodbye😊")
   else:
      print("Invalid Option")
      print("Try Again.....")        