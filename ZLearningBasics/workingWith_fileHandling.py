        #CREATING A NEW FILE USING FILE=OPEN()

file=open("Student.txt","w")
file.write("1234 AYUSHBABITARAHULSAURAVRAKESH")
file.close()

        #READING THE FILE DATA USING READ(),READLINE(),READLINES()
file=open("Student.txt","r")
Data=file.readlines()
file.close()
#print(Data)


        #UPDATION OF THE EXISTING FILE USING: "a"

file=open("Student.txt","a")
file.write("PYTHONCBOTHTMLCSS")        
file.close()

file=open("Student.txt","r")
updateData=file.read()
file.close()
#print(updateData)


        #updating file data and reading at the same time a+
file=open("Student.txt","a+")
file.write("C++")
file.seek(0)  #it will move the pointer again to the first element of the file
newData=file.read()
#print(newData)        
file.close()



                #file pointers METHOD 1

#with open("Student.txt","r")as file:
    #print(file.read(5))                
    #print(file.read(8)) 



                #file pointers METHOD 2

file = open("Student.txt","r")
#print(file.read(5))
#print(file.read(5))
#print(file.tell()) #to get the pointer value
file.seek(0)
#print(file.read())
updates=["SATYAM","SHIVAM","SAI"]
file=open("Student.txt","a")
file.writelines(updates)
file.close()
file=open("Student.txt","r")
#print(file.read())
file.close()

# file=open("Student.txt","r")
# text=file.read()
# file.close()
# file=open("Student.txt","w")
# text=text.replace("AYUSH","ANISH")
# file.write(text)

with open("Student.txt","r") as file:
    text=file.read()  #storing all data in a new text named variable


text=text.replace("AYUSH","A N I S H")    #using text.replace to replace some specific content

with open("Student.txt","w") as file:
    file.write(text)  #re arranging the data in the main file with updated data

#with open("Student.txt","r") as file:
    #print(file.read())    #prints the data

  


#USED TO CHECK IF FILE IS THERE IN THE WORKING FOLDER OR NOT
# import os #CALLING OPERATING SYSTEM
# if os.path.exists("TESTSHEET.py"):#ASKING OS TO THE PATH AND FILE NAME IF IT EXISTS?
#     print("File exists!")
# else:
#     print("Fine not found")    


#import os
# if os.path.exists("number.txt"):
#     os.remove("number.txt")
#     print("DONE!!")
# else:
#     print("file not found")




# if os.path.exists("number.txt"):
#     print("yes!!")    
# else:
#     print("NO")    



# import os
# if not os.path.exists("MyFolder"):
#     os.mkdir("MyFolder")
#     print("folder created!")
# else:
#     print("folder exists!")    




  