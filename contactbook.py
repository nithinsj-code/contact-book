contacts = {}

while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully.")

    elif choice == "2":
        if ocntacts == {}:
            print("No contacts found.")
        else:
            print("\n--- ALL CONTACTS ---")
            for name in contacts:
                print("Name:", name)
                print("Phone:", contacts[name]["phone"])
                print("Email:", contacts[name]["email"])
                print("------------------")

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in contacts:
            print("Name:", search)
            print("Phone:", contacts[search]["phone"])
            print("Email:", contacts[search]["email"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you! Exiting Contact Book.")
        break

    else:
        print("Invalid choice. Try again.")
