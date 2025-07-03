contacts = {
    "Ali": {
        "phone": "123",
        "email": "ali@email.com"
    }

}
def update_contact():
    name_to_update = input("Which contact do you want to update")
    name_to_update = name_to_update.title()

    if name_to_update in contacts:
        phone = input("Enter new phone number: ")

        while True:
            email = input("Enter new email address" )
            if "@" in email and "." in email:
                break
            else:
                print("Invalid email.Please include @ and ","in the email")

        contacts[name_to_update] = {"phone":phone,"email":email}
        print(f"Contact for {name_to_update} added succesfully")
    else:
        print("Contact not found")

def add_contact():
     
    name = input("Enter your name : ")
    name = name.title()
    if name in contacts:
         print("Contact already exists.Cannot add duplicate")
         return
    phone = input("Enter your phone : ")
    while True:
         email = input("Enter your email: ")
         if "@" in email and "." in email:
              break
         else:
              print("Invalid email.Please include @ and ","in the email")
    contacts[name]  = {"phone": phone, "email" : email}
    print(f"Contact for {name} added succesfully")


def retreive_contact():
     contact = input("Which contact do you want to retrieve?")
     contact = contact.title()
     if contact in contacts:
        print(f"Phone: {contacts[contact]['phone']}, Email: {contacts[contact]['email']}")
     else:
          print("Not Found")

def view_all_contacts():
     if not  contacts:
        print("No contacts found")
     else:
          for contact in contacts:
               phone = contacts[contact]["phone"]
               email = contacts[contact]["email"]
               print(f"{contact} : Phone : {phone},Email:{email}")
                 
while True:
     user_choice = input("Pick and option by entering  a number between 1 and 5 : ")
     if user_choice == "1":
          print("1. Add Contact")
          add_contact()
     elif user_choice == "2":
          print("2. Update Contact")
          update_contact()
     elif user_choice == "3":
           print("3. Retrieve  Contact")  
           retreive_contact() 
     elif user_choice == "4":
          print("4. View All Contact")
          view_all_contacts()
     elif user_choice == "5":
           print("5. Exit ")
           break 
     else:
          print("Enter a valid choice between 1-5")

         

    
        
    


    

    
    
        
    
    
    


    