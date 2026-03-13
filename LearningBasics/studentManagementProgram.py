students={}
def add_student():
    roll=int(input("Enter roll number: "))
    if roll in students:
        print("Student already exists!")
        return
    name = input("Enter name: ")
    marks = int (input("Enter marks: "))
    students[roll]={
        "name":name,
        "marks": marks
    }

def view_students():
    if not students:
        return
    for roll, info in students.items():
        print("Roll-No:",roll)
        print("Name: ",info["name"])
        print("Marks: ",info["marks"])
        print("- "*20)    


def search_students():
    roll=int(input("Enter roll no to SEARCH: "))
    if roll in students:
        info = students[roll]
        print("Name: ",info["name"])
        print("Marks: ",info["marks"])
    else:
        print("Student not found!!")    

def update_marks():
    roll=int(input("Eneter roll no: "))
    if roll in students:
        new_marks = int(input("Enter new marks: "))
        students[roll]["marks"]=new_marks
        print("Marks updated!")
    else:
        print("Student not found!!")    

def delete_student():
    roll = int(input("Enter roll no: "))
    if roll in students:
        students.pop(roll)
        print("Student record Deleted!")
    else:
        print("Student not found!")

def main():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        match (choice):
            case 1:
                add_student()
            case 2:
                view_students()
            case 3:
                search_students()
            case 4:
                update_marks()
            case 5:
                delete_student()
            case 6:
                print("Exitting program....")
                break                   
            
main()            


