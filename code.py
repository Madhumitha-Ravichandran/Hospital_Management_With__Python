while (True):
    print("""
            ================================
               Welcome To CityHospital
            ================================
    """)
    ##creating database connectivity
    import mysql.connector
    passwd = str(input("Enter the Password Please!!:"))

    mysql = mysql.connector.connect(host="localhost", user="root", passwd="your password")
    mycursor = mysql.cursor()
    mycursor.execute("create database if not exists city_hospitals")
    mycursor.execute("use city_hospitals")
    # creating the tables we need
    mycursor.execute("create table if not exists patient_detail(name varchar(30) primary key,sex varchar(15),age int(3),address varchar(50),contact varchar(15))")
    mycursor.execute("create table if not exists doctor_details(name varchar(30) primary key,specialisation varchar(40),age int(2),address varchar(30),contact varchar(15),fees int(10),monthly_salary int(10))")
    mycursor.execute("create table if not exists nurse_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")
    mycursor.execute("create table if not exists other_workers_details(name varchar(30) primary key,age int(2),address varchar(30),contact varchar(15),monthly_salary int(10))")
  
    # creating table for storing the username and password of the user
    mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")
  
    while (True):
        print("""
                        1. Sign In
                        2. Registration
                                                            """)

        r = int(input("enter your choice:"))
        if r == 2:
            print("""

                =======================================
                !!!!!!!!!!Register Yourself!!!!!!!!
                =======================================
                                                    """)
            u = input("Input your username!!:")
            p = input("Input the password (Password must be strong!!!:")
            mycursor.execute("insert into user_data values('" + u + "','" + p + "')")
            mysql.commit()

            print("""
                ============================================
                !!Well Done!!Registration Done Successfully!!
                ============================================
                                                    """)
            x = input("enter any key to continue:")
        # IF USER WANTS TO LOGIN
        elif r == 1:
            print("""
                    ==================================
                    !!!!!!!!  {{Sign In}}  !!!!!!!!!!
                    ==================================
                                                        """)
            un = input("Enter Username!!:")
            ps = input("Enter Password!!:")

            mycursor.execute("select password from user_data where username='" + un + "'")
            row = mycursor.fetchall()
            for i in row:
                a = list(i)
                if a[0] == str(ps):
                    while (True):
                        print("""
                                1.Administration
                                2.Patient(Details)
                                3.Sign Out

                                                            """)

                        a = int(input("ENTER YOUR CHOICE:"))
                        if a == 1:
                            print("""
                                    1. Display the details
                                    2. Add a new member
                                    3. Delete a member
                                    4. Make an exit
                                                             """)
                            b = int(input("Enter your Choice:"))
                            #details 
                            if b == 1:
                                print("""
                                        1. Doctors Details
                                        2. Nurse Details
                                        3. Others
                                                         """)

     
                                c = int(input("Enter your Choice:"))
                         if c == 1:
                                    mycursor.execute("select * from doctor_details")
                                    row = mycursor.fetchall()
                                    for i in row:
                                        b = 0
                                        v = list(i)
                                        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "FEES",
                                             "MONTHLY_SALARY"]
                                        d = dict(zip(k, v))
                                        print(d)
                                #displays nurses details
                                elif c == 2:
                                    mycursor.execute("select * from nurse_details")
                                    row = mycursor.fetchall()
                                    for i in row:
                                        v = list(i)
                                        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "MONTHLY_SALARY"]
                                        d = dict(zip(k, v))
                                        print(d)
                                #displays worker details
                                elif c == 3:
                                    mycursor.execute("select * from other_workers_details")
                                    row = mycursor.fetchall()
                                    for i in row:
                                        v = list(i)
                                        k = ["NAME", "SPECIALISATION", "AGE", "ADDRESS", "CONTACT", "MONTHLY_SALARY"]
                                        d = dict(zip(k, v))
                                        print(d)
                            # IF USER WANTS TO ENTER DETAILS
                            elif b == 2:
                                print("""

                                        1. Doctor Details
                                        2. Nurse Details
                                        3. Others
                                                                                    """)
                                c = int(input("ENTER YOUR CHOICE:"))
                                # enter doctor details
                                if c == 1:
                                    # ASKING THE DETAILS
                                    name = input("Enter the doctor's name")
                                    spe = input("Enter the specilization:")
                                    age = input("Enter the age:")
                                    add = input("Enter the address:")
                                    cont = input("Enter Contact Details:")
                                    fees = input("Enter the fees:")
                                    ms = input("Enter Monthly Salary:")
                                    # Inserting values in doctors details
                                    mycursor.execute("insert into doctor_details values('" + name + "','" + spe + "','" + age + "','" + add + "','" + cont + "','" + fees + "','" + ms + "')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                                # for nurse details
                                elif c == 2:
                                    # ASKING THE DETAILS
                                    name = input("Enter Nurse name:")
                                    age = input("Enter age:")
                                    add = input("Enter address:")
                                    cont = input("Enter Contact No:")
                                    ms = int(input("Enter Monthly Salary"))
                                    # INSERTING VALUES ENTERED TO THE TABLE
                                    mycursor.execute("insert into nurse_details values('" + name + "','" + age + "','" + add + "','" + cont + "','" + str(
                                            ms) + "')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                                # for entering workers details
                                elif c == 3:
                                    # ASKING THE DETAILS
                                    name = input("Enter worker name:")
                                    age = input("Enter age:")
                                    add = input("Enter address:")
                                    cont = input("Enter Contact No.:")
                                    ms = input("Enter Monthly Salary:")
                                    # INSERTING VALUES ENTERED TO THE TABLE
                                    mycursor.execute("insert into other_workers_details values('" + name + "','" + age + "','" + add + "','" + cont + "','" + ms + "')")
                                    mysql.commit()
                                    print("SUCCESSFULLY ADDED")
                            #to delete data
                            elif b == 3:
                                print("""
                                        1. Doctor Details
                                        2. Nurse Details
                                        3. Others
                                                                                    """)
                                c = int(input("Enter your Choice:"))
                                # deleting doctor's details
                                if c == 1:
                                    name = input("Enter Doctor's Name:")
                                    mycursor.execute("select * from doctor_details where name='" + name + "'")
                                    row = mycursor.fetchall()
                                    print(row)
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        mycursor.execute("delete from doctor_details where name='" + name + "'")
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")


                                # deleting nurse details
                                elif c == 2:
                                    name = input("Enter Nurse Name:")
                                    mycursor.execute("select * from nurse_details where name='" + name + "'")
                                    row = mycursor.fetchall()
                                    print(row)
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        mycursor.execute("delete from nurse_details where name='" + name + "'")
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                                # deleting other_workers details
                                elif c == 3:
                                    name = input("Enter the worker Name")
                                    mycursor.execute("select * from workers_details where name='" + name + "'")
                                    row = mycursor.fetchall()
                                    print(row)
                                    p = input("you really wanna delete this data? (y/n):")
                                    if p == "y":
                                        mycursor.execute("delete from other_workers_details where name='" + name + "'")
                                        mysql.commit()
                                        print("SUCCESSFULLY DELETED!!")
                                    else:
                                        print("NOT DELETED")
                            elif b == 4:
                                break

                        # entering the patient details table
                        elif a == 2:

                            print("""
                                        1. Show Patients Info
                                        2. Add New Patient
                                        3. Discharge Summary
                                        4. Exit
                                                               """)
                            b = int(input("Enter your Choice:"))
                            # showing the existing details
                            # if user wants to see the details of PATIENT
                            if b == 1:
                                mycursor.execute("select * from patient_detail")
                                row = mycursor.fetchall()
                                for i in row:
                                    b = 0
                                    v = list(i)
                                    k = ["NAME", "SEX", "AGE", "ADDRESS", "CONTACT"]
                                    d = dict(zip(k, v))
                                    print(d)

                            # adding new patient
                            elif b == 2:
                                name = input("Enter your name ")
                                sex = input("Enter the gender: ")
                                age = input("Enter age: ")
                                address = input("Enter address: ")
                                contact = input("Contact Details: ")
                                mycursor.execute("insert into patient_detail values('" + name + "','" + sex + "','" +
                                        age + "','" + address + "','" + contact + "')")
                                mysql.commit()
                                mycursor.execute("select * from patient_detail")
                                for i in mycursor:
                                    v = list(i)
                                    k = ['NAME', 'SEX', 'AGE', 'ADDRESS', 'CONTACT']
                                    print(dict(zip(k, v)))
                                    print("""
                                        ====================================
                                        !!!!!!!Registered Successfully!!!!!!
                                        ====================================
                                                        """)
                            # dischare process
                            elif b == 3:
                                name = input("Enter the Patient Name:")
                                mycursor.execute("select * from patient_detail where name='" + name + "'")
                                row = mycursor.fetchall()
                                print(row)
                                bill = input("Has he paid all the bills? (y/n):")
                                if bill == "y":
                                    mycursor.execute("delete from patient_detail where name='" + name + "'")
                                    mysql.commit()
                            # if user wants to exit
                            elif b == 4:
                                break
                        ###SIGN OUT

                        elif a == 3:
                            break


                # IF THE USERNAME AND PASSWORD IS NOT IN THE DATABASE
                else:
                    break
import Read_Hospital_Excel_Sheet
import Write_Hospital_Excel_Sheet


def AppointmentIndexInDoctorsDataBase(patient_ID):
    for i in Doctors_DataBase:
        for j in Doctors_DataBase[i]:
            if str(patient_ID) == str(j[0]):
                Appointment_index = Doctors_DataBase[i].index(j)
                return Appointment_index, i


print("****************************************************************************")
print("*                                                                          *")
print("*                   Welcome Himamaylan Hospital Management System          *")
print("*                                                                          *")
print("****************************************************************************")

tries = 0
tries_flag = ""
while tries_flag != "Close the program":

    Pateints_DataBase = Read_Hospital_Excel_Sheet.Read_Patients_DataBase()
    Doctors_DataBase = Read_Hospital_Excel_Sheet.Read_Doctors_DataBase()

    print("-----------------------------------------")
    print("|Enter 1 for Admin mode			|\n|Enter 2 for user mode|")
    print("-----------------------------------------")
    Admin_user_mode = input("Enter your mode : ")

    if Admin_user_mode == "1":  # Admin mode
        print(
            "*****\n|         Welcome to admin mode         |\n*****")
        Password = input("Please enter your password : ")
        while True:

            if Password == "1234":
                print("-----------------------------------------")
                print("|To manage patients Enter 1|\n|"
                    "To manage docotrs Enter 2|\n|"
                    "To manage appointments Enter 3|\n|"
                    "To be back Enter E			|")
                print("-----------------------------------------")
                AdminOptions = input("Enter your choice : ")
                AdminOptions = AdminOptions.upper()

                if AdminOptions == "1":  # Admin mode --> Pateints Management
                    print("-----------------------------------------")
                    print("|To add new patient Enter 1	  	|")
                    print("|To display patient Enter 2	  	|")
                    print("|To delete patient data Enter 3		|")
                    print("|To edit patient data Enter 4    	|")
                    print("|To Back enter B      			|")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Pateints Management --> Enter new patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID in Pateints_DataBase:  # if Admin entered used ID
                                patient_ID = int(input("This ID is unavailable, please try another ID : "))
                            Department = input("Enter patient department                : ")
                            DoctorName = input("Enter name of doctor following the case : ")
                            Name = input("Enter patient name                      : ")
                            Age = input("Enter patient age                       : ")
                            Gender = input("Enter patient gender                    : ")
                            Address = input("Enter patient address                   : ")
                            RoomNumber = input("Enter patient room number               : ")
                            Pateints_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address,
                                                             RoomNumber]
                            print("----------------------Patient added successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Pateints Management --> Display patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            print("\npatient name        : ", Pateints_DataBase[patient_ID][2])
                            print("patient age         : ", Pateints_DataBase[patient_ID][3])
                            print("patient gender      : ", Pateints_DataBase[patient_ID][4])
                            print("patient address     : ", Pateints_DataBase[patient_ID][5])
                            print("patient room number : ", Pateints_DataBase[patient_ID][6])
                            print("patient is in " + Pateints_DataBase[patient_ID][0] + " department")
                            print("patient is followed by doctor : " + Pateints_DataBase[patient_ID][1])
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Pateints Management --> Delete patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            Pateints_DataBase.pop(patient_ID)
                            print("----------------------Patient data deleted successfully----------------------")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Pateints Management --> Edit patient data
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect ID, Please Enter patient ID : "))
                            while True:
                                print("------------------------------------------")
                                print("|To Edit pateint Department Enter 1 :    |")
                                print("|To Edit Doctor following case Enter 2 : |")
                                print("|To Edit pateint Name Enter 3 :          |")
                                print("|To Edit pateint Age Enter 4 :           |")
                                print("|To Edit pateint Gender Enter 5 :        |")
                                print("|To Edit pateint Address Enter 6 :       |")
                                print("|To Edit pateint RoomNumber Enter 7 :    |")
                                print("|To be Back Enter B                      |")
                                print("-----------------------------------------")
                                Admin_choice = input("Enter your choice : ")
                                Admin_choice = Admin_choice.upper()
                                if Admin_choice == "1":
                                    Pateints_DataBase[patient_ID][0] = input("\nEnter patient department : ")
                                    print(
                                        "----------------------Patient Department edited successfully----------------------")

                                elif Admin_choice == "2":
                                    Pateints_DataBase[patient_ID][1] = input("\nEnter Doctor follouing case : ")
                                    print(
                                        "----------------------Doctor follouing case edited successfully----------------------")

                                elif Admin_choice == "3":
                                    Pateints_DataBase[patient_ID][2] = input("\nEnter patient name : ")
                                    print(
                                        "----------------------Patient name edited successfully----------------------")

                                elif Admin_choice == "4":
                                    Pateints_DataBase[patient_ID][3] = input("\nEnter patient Age : ")
                                    print("----------------------Patient age edited successfully----------------------")

                                elif Admin_choice == "5":
                                    Pateints_DataBase[patient_ID][4] = input("\nEnter patient gender : ")
                                    print(
                                        "----------------------Patient address gender successfully----------------------")

                                elif Admin_choice == "6":
                                    Pateints_DataBase[patient_ID][5] = input("\nEnter patient address : ")
                                    print(
                                        "----------------------Patient address edited successfully----------------------")

                                elif Admin_choice == "7":
                                    Pateints_DataBase[patient_ID][6] = input("\nEnter patient RoomNumber : ")
                                    print(
                                        "----------------------Patient RoomNumber edited successfully----------------------")

                                elif Admin_choice == "B":
                                    break

                                else:
                                    print("Please Enter a correct choice")
                        except:
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "B":  # Admin mode --> Pateints Management --> Back
                        break

                    else:
                        print("Please enter a correct choice\n")

                elif AdminOptions == "2":  # Admin mode --> Doctors Management
                    print("-----------------------------------------")
                    print("|To add new doctor Enter 1              |")
                    print("|To display doctor Enter 2              |")
                    print("|To delete doctor data Enter 3          |")
                    print("|To edit doctor data Enter 4            |")
                    print("|To be back enter B                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()

                    if Admin_choice == "1":  # Admin mode --> Doctors Management --> Enter new doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID in Doctors_DataBase:  # if Admin entered used ID
                                Doctor_ID = int(input("This ID is unavailable, please try another ID : "))

                            Department = input("Enter Doctor department : ")
                            Name = input("Enter Doctor name       : ")
                            Address = input("Enter Doctor address    : ")
                            Doctors_DataBase[Doctor_ID] = [[Department, Name, Address]]
                            print("----------------------Doctor added successfully----------------------")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Doctors Management --> Display doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            print("Doctor name    : ", Doctors_DataBase[Doctor_ID][0][1])
                            print("Doctor address : ", Doctors_DataBase[Doctor_ID][0][2])
                            print("Doctor is in " + Doctors_DataBase[Doctor_ID][0][0] + " department")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Doctors Management --> Delete doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter doctor ID : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            Doctors_DataBase.pop(Doctor_ID)
                            print("/----------------------Doctor data deleted successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "4":  # Admin mode --> Doctors Management --> Edit Doctor data
                        try:  # To avoid non integer input
                            Doctor_ID = input("Enter doctor ID : ")
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Incorrect ID, Please Enter doctor ID : "))
                            print("-----------------------------------------")
                            print("|To Edit doctor's department Enter 1    |")
                            print("|To Edit doctor's name Enter 2          |")
                            print("|To Edit doctor's address Enter 3       |")
                            print("To be Back Enter B                      |")
                            print("-----------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                Doctors_DataBase[Doctor_ID][0][0] = input("Enter Doctor's Department : ")
                                print(
                                    "/----------------------Doctor's department edited successfully----------------------/")

                            elif Admin_choice == "2":
                                Doctors_DataBase[Doctor_ID][0][1] = input("Enter Doctor's Name : ")
                                print("----------------------Doctor's name edited successfully----------------------")

                            elif Admin_choice == "3":
                                Doctors_DataBase[Doctor_ID][0][2] = input("Enter Doctor's Address : ")
                                print(
                                    "----------------------Doctor's address edited successfully----------------------")

                            elif Admin_choice == "B":
                                break

                            else:
                                print("\nPlease enter a correct choice\n")

                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "B":  # Back
                        break

                    else:
                        print("\nPlease enter a correct choice\n")

                elif AdminOptions == "3":  # Admin mode --> Appointment Management
                    print("-----------------------------------------")
                    print("|To book an appointment Enter 1         |")
                    print("|To edit an appointment Enter 2         |")
                    print("|To cancel an appointment Enter 3       |")
                    print("|To be back enter B                     |")
                    print("-----------------------------------------")
                    Admin_choice = input("Enter your choice : ")
                    Admin_choice = Admin_choice.upper()
                    if Admin_choice == "1":  # Admin mode --> Appointment Management --> Book an appointment
                        try:  # To avoid non integer input
                            Doctor_ID = int(input("Enter the ID of doctor : "))
                            while Doctor_ID not in Doctors_DataBase:
                                Doctor_ID = int(input("Doctor ID incorrect, Please enter a correct doctor ID : "))
                            print("---------------------------------------------------------")
                            print("|For book an appointment for an exist patient Enter 1|\n|"
                                  "For book an appointment for a new patient Enter 2|\n|"
                                  "To be Back Enter B|")
                            print("---------------------------------------------------------")
                            Admin_choice = input("Enter your choice : ")
                            Admin_choice = Admin_choice.upper()
                            if Admin_choice == "1":
                                patient_ID = int(input("Enter patient ID : "))
                                while patient_ID not in Pateints_DataBase:  # if Admin entered incorrect ID
                                    patient_ID = int(input("Incorrect ID, please Enter a correct patient ID : "))


                            elif Admin_choice == "2":
                                patient_ID = int(input("Enter patient ID : "))
                                while patient_ID in Pateints_DataBase:  # if Admin entered used ID
                                    patient_ID = int(input("This ID is unavailable, please try another ID : "))
                                Department = Doctors_DataBase[Doctor_ID][0][0]
                                DoctorName = Doctors_DataBase[Doctor_ID][0][1]
                                Name = input("Enter patient name    : ")
                                Age = input("Enter patient age     : ")
                                Gender = input("Enter patient gender  : ")
                                Address = input("Enter patient address : ")
                                RoomNumber = ""
                                Pateints_DataBase[patient_ID] = [Department, DoctorName, Name, Age, Gender, Address,
                                                                 RoomNumber]

                            elif Admin_choice == "B":
                                break

                            Session_Start = input("Session starts at : ")
                            while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                Session_Start = input("Appointments should be between 01:00PM to 10:00PM,"
                                                      "Please enter a time between working hours : ")

                            for i in Doctors_DataBase[Doctor_ID]:
                                if type(i[0]) != str:
                                    while Session_Start >= i[1] and Session_Start < i[2]:
                                        Session_Start = input("This appointment is already booked,"
                                                              "Please Enter an other time for start of session : ")
                            Session_End = input("Session ends at : ")

                            New_Appointment = list()
                            New_Appointment.append(patient_ID)
                            New_Appointment.append(Session_Start)
                            New_Appointment.append(Session_End)
                            Doctors_DataBase[Doctor_ID].append(New_Appointment)
                            print("/----------------------Appointment booked successfully----------------------/")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "2":  # Admin mode --> Appointment Management --> Edit an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Incorrect Id, Please Enter correct patient ID : "))
                            try:  # To avoid no return function
                                AppointmentIndex, PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
                                Session_Start = input("Please enter the new start time : ")
                                while Session_Start[:2] == "11" or Session_Start[:2] == "12":
                                    Session_Start = input("Appointments should be between 01:00PM to 10:00PM,"
                                                          "Please enter a time between working hours : ")

                                for i in Doctors_DataBase[Doctor_ID]:
                                    if type(i[0]) != str:
                                        while Session_Start >= i[1] and Session_Start < i[2]:
                                            Session_Start = input("This appointment is already booked, "
                                                                  "Please Enter an other time for start of session : ")
                                Session_End = input("Please enter the new end time : ")
                                Doctors_DataBase[PairKey][AppointmentIndex] = [patient_ID, Session_Start, Session_End]
                                print("/----------------------appointment edited successfully----------------------/")
                            except:
                                print("No Appointment for this patient")
                        except:
                            print("Doctor ID should be an integer number")

                    elif Admin_choice == "3":  # Admin mode --> Appointment Management --> Cancel an appointment
                        try:  # To avoid non integer input
                            patient_ID = int(input("Enter patient ID : "))
                            while patient_ID not in Pateints_DataBase:
                                patient_ID = int(input("Invorrect ID, Enter patient ID : "))
                            try:
                                AppointmentIndex, PairKey = AppointmentIndexInDoctorsDataBase(patient_ID)
                                Doctors_DataBase[PairKey].pop(AppointmentIndex)
                                print("/----------------------appointment canceled successfully----------------------/")
                            except:
                                print("No Appointment for this patient")
                        except:  # To avoid no return function
                            print("Patient ID should be an integer number")

                    elif Admin_choice == "B":  # Back
                        break

                    else:
                        print("please enter a correct choice")

                elif AdminOptions == "B":  # Back
                    break

                else:
                    print("Please enter a correct option")


            elif Password != "1234":
                if tries < 2:
                    Password = input("Password incorrect, please try again : ")
                    tries += 1
                else:
                    print("Incorrect password, no more tries")
                    tries_flag = "Close the program"
                    break

            Write_Hospital_Excel_Sheet.Write_Patients_DataBase(Pateints_DataBase)
            Write_Hospital_Excel_Sheet.Write_Doctors_DataBase(Doctors_DataBase)


    elif Admin_user_mode == "2":  # User mode
        print("*****\n|         Welcome to user mode         |\n*****")
        while True:
            print("\n-----------------------------------------")
            print("|To view hospital's departments Enter 1 |")
            print("|To view hospital's docotrs Enter 2     |")
            print("|To view patients' residents Enter 3    |")
            print("|To view patient's details Enter 4      |")
            print("|To view doctor's appointments Enter 5  |")
            print("|To be Back Enter B                     |")
            print("-----------------------------------------")
            UserOptions = input("Enter your choice : ")
            UserOptions = UserOptions.upper()

            if UserOptions == "1":  # User mode --> view hospital's departments
                print("Hospital's departments :")
                for i in Doctors_DataBase:
                    print("	" + Doctors_DataBase[i][0][0])

            elif UserOptions == "2":  # User mode --> view hospital's Doctors
                print("Hospital's doctors :")
                for i in Doctors_DataBase:
                    print(
                        "	" + Doctors_DataBase[i][0][1] + " in " + Doctors_DataBase[i][0][0] + " department, from " +
                        Doctors_DataBase[i][0][2])

            elif UserOptions == "3":  # User mode --> view patients' residents
                for i in Pateints_DataBase:
                    print("	Patient : " + Pateints_DataBase[i][2] + " in " + Pateints_DataBase[i][
                        0] + " department and followed by " + Pateints_DataBase[i][1] + ", age : " +
                          Pateints_DataBase[i][3] + ", from : " + Pateints_DataBase[i][5] + ", RoomNumber : " +
                          Pateints_DataBase[i][6])

            elif UserOptions == "4":  # User mode --> view patient's details
                try:  # To avoid non integer input
                    patient_ID = int(input("Enter patient's ID : "))
                    while patient_ID not in Pateints_DataBase:
                        patient_ID = int(input("Incorrect Id, Please enter patient ID : "))
                    print("	patient name        : ", Pateints_DataBase[patient_ID][2])
                    print("	patient age         : ", Pateints_DataBase[patient_ID][3])
                    print("	patient gender      : ", Pateints_DataBase[patient_ID][4])
                    print("	patient address     : ", Pateints_DataBase[patient_ID][5])
                    print("	patient room number : ", Pateints_DataBase[patient_ID][6])
                    print("	patient is in " + Pateints_DataBase[patient_ID][0] + " department")
                    print("	patient is followed by doctor : " + Pateints_DataBase[patient_ID][1])
                except:
                    print("Patient ID should be an integer number")

            elif UserOptions == "5":  # User mode --> view doctor's appointments
                try:  # To avoid non integer input
                    Doctor_ID = int(input("Enter doctor's ID : "))
                    while Doctor_ID not in Doctors_DataBase:
                        Doctor_ID = int(input("Incorrect Id, Please enter doctor ID : "))
                    print(Doctors_DataBase[Doctor_ID][0][1] + " has appointments :")
                    for i in Doctors_DataBase[Doctor_ID]:
                        if type(i[0]) == str:
                            continue
                        else:
                            print("	from : " + i[1] + "    to : " + i[2])
                except:
                    print("Doctor ID should be an integer number")

            elif UserOptions == "B":  # Back
                break

            else:
                print("Please Enter a correct choice")


    else:
        print("Please choice just 1 or 2")
