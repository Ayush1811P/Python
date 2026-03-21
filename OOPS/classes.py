
        #PROGRAM:  1

# class students:
#     print("Welcome to the students history!")
#     name="Ayush"
#     age=23
#     course="BCA"
#     def students():
#         print("I am cunstructor!")

#     def display(self):
#         print(f"Hello, {self.name} your age is: {self.age}")

# s1=students()
# s1.display()



        #PROGRAM:  2

# class dog:
#     def __init__(self,name):
#         self.name=name
#     def bark(self):
#         return f"{self.name} barks"
    
# Dog=dog("PONTY")    
# print(Dog.bark())



        #PROGRAM:  3

# class person:
#     name="USER"
#     age=0
#     city="unknown"

#     def introduce(self):
#         print(f"Hello,i'm {self.name} i'm {self.age} years old  from {self.city}")

# p1=person()
# p1.name="Ayush"
# p1.age=23
# p1.city="Noida"
# p1.introduce()



        #PROGRAM:  4

# class person:
#     def __init__(self,name,age,city):
#         self.name=name
#         self.age=age
#         self.city=city
#     def introduce(self):
#         print(f"Hello,i'm {self.name} i'm {self.age} from {self.city}")  

# p1=person("Ayush",23,"Noida")
# p1.introduce()




        #PROGRAM:  5

# class students:
#     def __init__(self,name,id,grade,marks=0):
#         self.name=name
#         self.id=id
#         self.grade=grade
#         self.marks=marks
      
#     def greet(self):
#             print("========================================")
#             return(f"hello i'm {self.name} my id is {self.id} \nMy grade is:{self.grade} and marks = {self.marks}")
#     def is_passed(self):
#         print("========================================")
#         if self.marks>40:
#             return("pass")
#         else:
#             return("Fail!")

# s1=students("Ayush",18,"A",76)

# print(s1.greet())
# print(s1.is_passed())



                #PROGRAM:  6


# class Student:
#     total_student=0
#     def __init__(self,name,id,grade,marks=0):
#         self.name=name
#         self.id=id
#         self.grade=grade
#         self.marks=marks
#         Student.total_student+=1
#     def greet(self):
#          print("*"*40)
#          return(f"hello i'm {self.name} my id is {self.id} \nMy grade is:{self.grade} and marks = {self.marks}")
#     def is_passed(self):
#         return "pass" if self.marks> 40 else "Fail"    
#     @classmethod
#     def get_total_students(cls):
#         return f"Total students: {cls.total_student}"
#     @staticmethod
#     def is_valid_marks(marks):
#         return 0 <= marks <= 100
    
# s1=Student("Ayush",18,"A", 85)    
# s2=Student("Ayushi",19,"B", 100) 
# print(s1.greet())
# print(s1.is_passed())
# print(s1.is_valid_marks(85))   
# print("/n" + Student.get_total_students())
