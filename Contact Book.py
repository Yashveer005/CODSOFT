                      #CONTACT BOOK

contacts = []

def add_contact(name, phone, email, address):
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts available.")

def search_contact(keywpord):
    found -= False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"Nmae: {contact['name']}, Phone: {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact(name, phone, email, address):
    for contact in contacts:
        if contact['name'] == name:
            contact.update({"phone": phone, "email": email, "address": address})
            print("Contact updated successfully.")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact['name']== name:
            contacts.remove(contact)
            print("Contact not found.")
            
                          #USER INTERFACE  
while True:
    print("\nMenu:")
    print("1. ADD CONTACT")
    print("2. VIEW CONTACT DETAILS") 
    print("3. SEARCH CONTACT") 
    print("4. UPDATE CONTACT") 
    print("5. DELETE CONTACT") 
    print("6. EXIT")

    choice = input("Enter your choice:")

    if choice == "1":
        name = input("Enter name:")
        phone = input("Enter phone number:")
        email = input("Enter email:")
        address = input("Enter address:")
        add_contact(name, phone, email, address) 

    elif choice == "2":
        print("Contact List:")
        view_contacts()

    elif choice == "3":
        keyword = input("Enter name or phone number to search")
        search_contact(keyword)

    elif choice == "4":
       name = input("Enter name of contact to update:")
       phone = input("Enter new phone number:")
       email = input("Enter new email:")
       address = input("Enter new address:")
       update_contact(name, phone, email, address) 

    elif choice == "5":
        name = input("Enter name of contavct to delete:")
        delete_contact(name)

    elif choice == "6":
        print("Existing")
        break

    else:
        print("Invalid choice. Please enter a number 1 and 6.")