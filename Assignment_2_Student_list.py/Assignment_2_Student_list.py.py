
#Ismoil Boboev 
#SEVD Assignment 2
#The purpose of this Assignment: To prompt for student name to find out if student is in Dean's List 
#Last Updated: 9/12



#THe context 

#Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
#ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.

#Promting to ask for the name input 




print("Enter Student Name: ")
name = str(input())
if name == 'ZZZ' :
   # prints the quit message
        print(quit)
        quit() 
        


        ##prompt and checking for the gpa setting up 
print("Enter Student GPA, use numbers please: ")
gpa = float(input())
if 3.5 <= gpa <= 4.0:
  gpa = 'A' 
elif 3.25 <= gpa <= 3.5:
  gpa = 'B'
else:
 1.0 <= gpa <= 3.25
 gpa = 'C'
 

#This function will return name and the gpa of the given student 
if gpa == 'A':
    print ("Student:  " +str(name) + " made it to Dean's List ")
elif gpa == 'B':
    print("Student: " +str(name) + " made it to Honor Roll, nice try! ")
elif gpa == 'C':
    print ("Student: " +str(name) + " did not make it to Dean's List, wa, wa. " + str(name ) + " might have made it to some other list tho.")

