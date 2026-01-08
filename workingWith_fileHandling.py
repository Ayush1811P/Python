        #CREATING A NEW FILE USING FILE=OPEN()

file=open("Student.txt","w")
file.write("AYUSH\nBABITA\nRAHUL\nSAURAV\nRAKESH\n")
file.close()

        #READING THE FILE DATA USING READ(),READLINE(),READLINES()
file=open("Student.txt","r")
Data=file.readlines()
file.close()
#print(Data)


        #UPDATION OF THE EXISTING FILE USING: "a"

file=open("Student.txt","a")
file.write("PYTHON\nCBOT\nHTML\nCSS")        
file.close()

file=open("Student.txt","r")
updateData=file.read()
file.close()
#print(updateData)


        #updating file data and reading at the same time a+
file=open("Student.txt","a+")
file.write("\nC++")
file.seek(0)  #it will move the pointer again to the first element of the file
newData=file.read()
print(newData)        
file.close()


