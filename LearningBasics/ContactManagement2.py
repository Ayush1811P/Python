contacts = []
def add():
    name = input("Enter name: ")
    phone = input("Enter phone no. : ")

    contact ={
        "name":name,
        "phone":phone
    }
    contacts.append(contact)
    print("contact added successfullly") 


def display():
    if len(contacts)==0:
        print("no contacts found!")
    else:
        for contact in contacts:
            print("name: " ,contact["name"])
            print("phone: " ,contact["phone"])
            

def Delete():
    if len(contacts)==0:
        print("no contacts found!")
    else:
        name_delete=input("Enter name to delte:")
        for contact in contacts:
            if name_delete.lower()==contact["name"].lower():
                contacts.remove(contact)
                print("contact deleted!")

def main():
    while True:
        print("\n--- CONTACT MANAGEMENT SYSTEM ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
      
        choice = int(input("enter your choice: "))

        match choice:
            case 1:
                add()
            case 2:
                display()
            case 3:
                Delete()
            case 4:
                exit()

main()                            