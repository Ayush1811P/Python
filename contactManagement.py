class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("-" * 20)


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contact = Contact(name, phone)
        self.contacts.append(contact)

        print("Contact added successfully!")

    def view_contact(self):
        if len(self.contacts) == 0:
            print("No contacts found!")
        else:
            for contact in self.contacts:
                contact.display()

    def search_contact(self):
        search_name = input("Enter name to search: ")
        found = False

        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                contact.display()
                found = True
                break

        if not found:
            print("Contact does not exist")

    def delete_contact(self):
        delete_name = input("Enter name to delete: ")

        for contact in self.contacts:
            if contact.name.lower() == delete_name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully")
                return

        print("Contact not found!")


def main():
    manager = ContactManager()

    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                manager.add_contact()
            case "2":
                manager.view_contact()
            case "3":
                manager.search_contact()
            case "4":
                manager.delete_contact()
            case "5":
                print("Exiting...")
                break
            case _:
                print("Invalid choice")


main()
