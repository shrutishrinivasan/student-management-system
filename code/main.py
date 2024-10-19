import pickle
import statistics

def CreateStudentList():
    try:
        with open("STUDENT.DAT", "wb") as F:
         A=[];VAL=100
         while True:
            ANO="Q"+str(VAL)
            print("Admission no. assigned to student : "+ANO)           #0
            while True:
             NAME=str(input("Name of student : "))                      #1
             if NAME.isalpha() is True:                                 #To raise error if name is entered as a numeric value
                     break
             else:
                     print("Please enter only alphabets!")
            DOB=str(input("Date of birth (format:DD-MM-YY) : "))        #2
            CLASS=int(input("Class : "))                                #3
            SECTION=str(input("Section : "))                            #4
            AGE=int(input("Age : "))                                    #5
            GENDER=str(input("Gender : "))                              #6
            BLDGRP=str(input("Blood Group : "))                         #7
            ATTENDANCE=' '                                              #8  To be filled later on
            AVERAGE=' '                                                 #9  To be filled later on
            RESULT_GRADE =' '                                           #10 To be filled later on
            A.append([ANO, NAME, DOB, CLASS, SECTION, AGE, GENDER, BLDGRP, ATTENDANCE, AVERAGE, RESULT_GRADE])
            VAL+=1
            Q=input("Want to add more?(Y/N) ")
            Q=Q.strip()
            if Q in ['n', 'N']:
                break
         pickle.dump(A,F)
    except ValueError:
            print("Please enter the correct data type!")

def AddStudent(): #For admin login
    try:
        with open("STUDENT.DAT", "rb+") as F:
         A=pickle.load(F)
         X=int(len(A)-1)
         VAL=int(A[X][0][1::])+1
         while True:
            ANO="Q"+str(VAL)
            print("Admission no. assigned to student : "+ANO)
            while True:
             NAME=str(input("Name of student : "))    
             if NAME.isalpha() is True:               
                     break
             else:
                     print("Please enter only alphabets!")
            DOB=str(input("Date of birth (format:DD-MM-YY) : "))
            CLASS=int(input("Class : "))
            SECTION=str(input("Section : "))
            AGE=int(input("Age : "))
            GENDER=str(input("Gender : "))
            BLDGRP=str(input("Blood Group : "))
            ATTENDANCE=' '                        
            AVERAGE=' '                           
            RESULT_GRADE =' ' 
            A.append([ANO, NAME, DOB, CLASS, SECTION, AGE, GENDER, BLDGRP, ATTENDANCE, AVERAGE, RESULT_GRADE])
            VAL+=1
            Q=input("Want to add more?(Y/N) ")
            Q=Q.strip()
            if Q in ['n', 'N']:
                break
         F.seek(0)
         pickle.dump(A,F)
    except FileNotFoundError:
        print("File not found! Retry.")
    except ValueError:
        print("Please enter the correct data type!")
        
def AddYourself(): #For service login
    try:
        with open("STUDENT.DAT", "rb+") as F:
            A=pickle.load(F)
            X=int(len(A)-1)
            VAL=int(A[X][0][1::])+1
            ANO="Q"+str(VAL)
            print("Your admission no. : "+ANO) 
            while True:
             NAME=str(input("Name of student : "))
             if NAME.isalpha() is True:               
                     break
             else:
                     print("Please enter only alphabets!")
            DOB=str(input("Date of birth (format:DD-MM-YY) : "))
            CLASS=int(input("Class : "))
            SECTION=str(input("Section : "))
            AGE=int(input("Age : "))
            GENDER=str(input("Gender : "))
            BLDGRP=str(input("Blood Group : "))
            ATTENDANCE=' '                        
            AVERAGE=' '                           
            RESULT_GRADE =' ' 
            A.append([ANO, NAME, DOB, CLASS, SECTION, AGE, GENDER, BLDGRP, ATTENDANCE, AVERAGE, RESULT_GRADE])
            F.seek(0)
            pickle.dump(A,F)
    except FileNotFoundError:
        print("File not found! Retry.")
    except ValueError:
        print("Please enter the correct data type!")

def ViewDetails(): #For admin login
    try:
        with open("STUDENT.DAT", "rb") as F:
            A=pickle.load(F)
            for i in A:
                print(i)
    except FileNotFoundError:
        print("File not found! Retry.")

def ViewYourDetails(): #For service login
    try:
        with open("STUDENT.DAT", "rb") as F:
            A=pickle.load(F)
            Q=input("Enter your admission no. to view your details : ")
            for i in A:
                if Q==i[0]:
                        print(i)
                        break
            else:
                    print("Admission no. not found!")
    except FileNotFoundError:
        print("File not found! Retry.")
    
def ModifyDetails():
    try:
        with open("STUDENT.DAT", "rb+") as F:
            A=pickle.load(F)
            Q=input("Enter student admission no. whose details have to be modified : ")
            for i in A:
                if Q==i[0]:
                    S=input("Enter which detail has to be modified (NAME/DOB/CLASS/SECTION/AGE/GENDER/BLDGRP/ATD/AVG/RESULT) : ")
                    if S=="NAME":
                        i[1]=input("Enter new student name : ")
                        print("Record Updated.")
                    elif S=="DOB":
                        i[2]=input("Enter new date of birth : ")
                        print("Record Updated.")
                    elif S=="CLASS":
                        i[3]=int(input("Enter new class : "))
                        print("Record Updated.")
                    elif S=="SECTION":
                        i[4]=input("Enter new section : ")
                        print("Record Updated.")
                    elif S=="AGE":
                        i[5]=int(input("Enter new age : "))
                        print("Record Updated.")
                    elif S=="GENDER":
                        i[6]=input("Enter new gender : ")
                        print("Record Updated.")
                    elif S=="BLDGRP":
                        i[7]=input("Enter new blood group : ")
                        print("Record Updated.")
                    elif S=="ATD":
                        i[8]=int(input("Enter new attendance: "))
                        print("Record Updated.")
                    elif S=="AVG":
                        i[9]=int(input("Enter new percentage : "))
                        print("Record Updated.")
                    elif S=="RESULT":
                        i[10]=input("Enter new result : ")
                        print("Record Updated.")
                    else:
                        print("Invalid Entry!")
                    break
            else:
                print("Admission no. not found!")
            F.seek(0)
            pickle.dump(A,F)
    except FileNotFoundError:
        print("File not found! Retry.")
    except ValueError:
        print("Please enter correct data type!")

def DeleteStudentRecord():
    try:
        with open("STUDENT.DAT", "rb+") as F:
            A=pickle.load(F)
            Q=input("Enter student admission no. whose record has to be deleted : ")
            for i in A:
                if Q==i[0]:
                    Z=A.index(i)
                    A.pop(Z)
                    print("Student record deleted.")
                    break
            else:
                print("Admission no. not found!")
            F.seek(0)
            pickle.dump(A,F)
    except FileNotFoundError:
        print("File not found! Retry.")

def Male_Female():
    with open("STUDENT.DAT", "rb") as F:
         A=pickle.load(F)
         d=[]; e=[]
         for i in A:
            if i[6] in ["Male", 'MALE']:
                d.append(i[1])
            elif i[6] in ["Female", 'FEMALE']:
                e.append(i[1])
         print(d, "Count of male students: ", len(d))
         print(e, "Count of female students: ", len(e))

def SearchStudent():
    try:
        with open("STUDENT.DAT", "rb") as F:
            A=pickle.load(F)
            Q=input("Enter student admission no. whose record has to be displayed : ")
            for i in A:
                    if Q==i[0]:
                        print(i)
                        break
            else:
                    print("Admission no. not found!")
    except FileNotFoundError:
        print("File not found! Retry.")

def SortAlphabeticalOrder():
    try:
        with open("STUDENT.DAT", "rb") as F:
            A=pickle.load(F)
            B=[]
            for i in A:
                B.append(i[1])
            B.sort()
            print(B)
    except FileNotFoundError:
        print("File not found! Retry.")

def GenerateAttendance(): #For Admin login
    try:
        with open("STUDENT.DAT", "rb+") as F:                     
         A=pickle.load(F)
         Q=input("Enter student admission no. to update attendance : ")
         for i in A:
             if Q==i[0]:
                 X=int(input("Enter student's attendance (for the academic session ie enter the no. of days attended out of 365) : "))
                 ATD=round(((X/365)*100),2)
                 print("Attendance percentage : ", ATD)
                 print("Attendance marked.")
                 i[8]=ATD
                 break
         else:
             print("Admission no. not found!")
         F.seek(0)
         pickle.dump(A,F)
    except FileNotFoundError:
        print("File not found! Retry.")

def ViewAttendance(): #For Service login
    try:
        with open("STUDENT.DAT", "rb") as F:                     
         A=pickle.load(F)
         Q=input("Enter your admission no. to know your attendance : ")
         for i in A:
             if Q==i[0]:
                if i[8]!=" ":
                 print("Attendance : ", i[8])
                 break
                elif i[8]==" ":
                 print("Your attendance has not been marked. Please inform your teacher.")
                 break
         else:
                 print("Admission no. not found!")
    except FileNotFoundError:
        print("File not found! Retry.")

def GenerateResult(): #For Admin login
     try:
        with open("STUDENT.DAT", "rb+") as F:                     
         A=pickle.load(F)
         B=[]
         Q=input("Enter student admission no. to update marks in record : ")
         for i in A:
          if Q==i[0]:
            print("Enter student marks in each subject...")
            while True:
                ENG=int(input("English : "))
                MATH=int(input("Maths : "))
                SCI=int(input("Science : "))
                SST=int(input("Social Studies : "))
                COMP=int(input("Computer Science : "))
                TL=int(input("Third Language : "))
                AVG=round(((ENG+MATH+SCI+SST+COMP+TL)/6),2)
                i[9]=AVG
                print("Student's overall percentage is: ", AVG)
                if AVG>=90 and AVG<=100:
                    R='PASS (A)'
                    i[10]=R
                    print("Student grade is : A")
                elif AVG>=80 and AVG<=89:
                    R='PASS (B)'
                    i[10]=R
                    print("Student grade is : B")
                elif AVG>=65 and AVG<=79:
                    R='PASS (C)'
                    i[10]=R
                    print("Student grade is : C")
                elif AVG>=40 and AVG<=64:
                    R='PASS (D)'
                    i[10]=R
                    print("Student grade is : D")
                elif AVG>=0 and AVG<=39:
                    R='FAIL'
                    i[10]=R
                    print("Student grade is : FAIL")
                break
            break
         else:
              print("Admission no. not found!")
         F.seek(0)
         pickle.dump(A,F)
     except FileNotFoundError:
        print("File not found! Retry.")
     except ValueError:
        print("Please enter the correct data type!")

def ViewResult(): #For Service login
    try:
        with open("STUDENT.DAT", "rb") as F:                     
         A=pickle.load(F)
         Q=input("Enter your admission no. to know your result: ")
         for i in A:
             if Q==i[0]:
                if i[9]!=" ":
                 print("Overall percentage : ", i[9])
                 print("Your Grade : ", i[10])
                 break
                elif i[9]==" ":
                 print("Your result has not been generated. Please inform your teacher.")
                 break
         else:
             print("Admission no. not found!")
    except FileNotFoundError:
        print("File not found! Retry.")

B=[];C=[];D=[]#For rank list     
def GenerateReport(): #For Admin login
    try:
     with open("STUDENT.DAT", "rb+") as F:
         A=pickle.load(F)
         print("Name     Date_of_Birth     Class     Section     Percentage     Result     Attendance")
         global B; global C; global D
         for i in A:
             print(i[1],"   ",i[2],"        ",i[3],"      ",i[4],"         ",i[9],"        ",i[10],"      ",i[8])
         for i in A:
           if i[9] not in B:
             B.append(i[9])
             C.append(i[10])
             D.append(i[8])
         print("The class average is : ", round(statistics.mean(B),2))
         x=max(B)
         for i in A:
            if i[9]==x:
                print("The class topper is : ", i[1])
                break
         PASS=[];FAIL=[]
         for i in A:
            if i[10]=="PASS (A)" or i[10]=="PASS (B)" or i[10]=="PASS (C)" or i[10]=="PASS (D)":
                PASS.append(i[1])
            elif i[10]=='FAIL':
                FAIL.append(i[1])
         print("No. of students who have passed : ", len(PASS), PASS)
         print("No. of students who have failed : ", len(FAIL), FAIL)
         y=max(D)
         for i in A:
            if i[8]==y:
                print("Student who has attended the most no. of days : ", i[1])
                break
         print("")
         print("Grading scheme is as follows:")
         print("A : 100-90")
         print("B : 89-80")
         print("C : 79-65")
         print("D : 64-40")
         print("FAIL : less than 40")
    except FileNotFoundError:
        print("File not found! Retry.")

def RankList():
    global B
    RANK=sorted(B)
    try:
        with open("STUDENT.DAT", "rb+") as F:                     
         A=pickle.load(F)
         LIST=[]
         for j in RANK:
             for i in A:
                 if i[9]==j:
                     LIST.append(i[1])
        print("Rank list is as follows:")
        print("Rank     Name")
        z=int(len(LIST))
        for k in range(0,z):
            print(k+1,"     ", LIST[z-k-1])
    except FileNotFoundError:
        print("File not found! Retry.")
        
def AdminLoginMenu():
      while True:
        print("")
        print("A : Create student list")
        print("B : Add new student")
        print("C : View details of all students")
        print("D : Modify details of a student")
        print("E : Delete a specific student's record")
        print("F : View no. of male and female students")
        print("G : Search a particular student")
        print("H : Arrange all students in an alphabetical order")
        print("I : Enter the attendance for a specific student")
        print("J : Enter marks for a specific student")
        print("K : Generate collective class report")
        print("L : Generate rank list")
        print("M : Quit application!")
        print("")
        print("Important Note: All empty fields will be filled later as you select different functions (Attendance and marks) to be executed")
        print("")
        Q=input("Enter your choice : ")
        Q=Q.strip()
        if Q=="A" or Q=="a":
            CreateStudentList()
        elif Q=="B" or Q=="b":
            AddStudent()
        elif Q=="C" or Q=="c":
            ViewDetails()
        elif Q=="D" or Q=="d":
            ModifyDetails()
        elif Q=="E" or Q=="e":
            DeleteStudentRecord()
        elif Q=="F" or Q=="f":
            Male_Female()
        elif Q=="G" or Q=="g":
            SearchStudent()
        elif Q=="H" or Q=="h":
            SortAlphabeticalOrder()
        elif Q=="I" or Q=="i":
            GenerateAttendance()
        elif Q=="J" or Q=="j":
            GenerateResult()
        elif Q=="K" or Q=="k":
                with open("STUDENT.DAT","rb") as F:
                        A=pickle.load(F)
                        LEN=len(A)
                        count=0
                        for i in A:
                                if i[8]!=" " and i[9]!=" " and i[10]!=" ":
                                        count+=1
                        if count==LEN:
                                GenerateReport()
                        else:
                                print("Please fill the empty entries first") 
        elif Q=="L" or Q=="l":
                with open("STUDENT.DAT","rb") as F:
                        A=pickle.load(F)
                        LEN=len(A)
                        count=0
                        for i in A:
                                if i[8]!=" " and i[9]!=" " and i[10]!=" ":
                                        count+=1
                        if count==LEN and B!=[]:
                                RankList()
                        else:
                                print("Please generate Collective Class Report first...")
        elif Q=="M" or Q=="m":
            break
        else:
            print("Invalid Entry!")
     
def StudentLoginMenu():
    while True:
        print("")
        print("A : Enter your personal details")
        print("B : Modify your details")
        print("C : Delete your record")
        print("D : View your details")
        print("E : Know your attendance")
        print("F : Know your result")
        print("G : Quit application!")
        print("")
        Q=input("Enter your choice : ")
        Q=Q.strip()
        if Q=="A" or Q=="a":
            AddYourself()
        elif Q=="B" or Q=="b":
            ModifyDetails()
        elif Q=="C" or Q=="c":
            DeleteStudentRecord()
        elif Q=="D" or Q=="d":
            ViewYourDetails()
        elif Q=="E" or Q=="e":
            ViewAttendance()
        elif Q=="F" or Q=="f":
            ViewResult()
        elif Q=="G" or Q=="g":
            break
        else:
            print("Invalid Entry!")

def FinalMenu():#For admin login and service login
    while True:
        Q=input("Enter your identity (ADMIN/STUDENT) OR (IF YOU WANT TO QUIT-Write EXIT): ")
        Q=Q.strip()
        if Q in ["ADMIN", "admin"]:
            PSWRD=input("Password : ") #Password="STAR" (sample)
            if PSWRD=="STAR":
                AdminLoginMenu()
            else:
                print("Wrong password. Entry denied!")
        elif Q in ["STUDENT", "student"]:
            StudentLoginMenu()
        elif Q in ["EXIT", "exit"]:
             break
        else:
            print("Invalid Entry!")

FinalMenu()
