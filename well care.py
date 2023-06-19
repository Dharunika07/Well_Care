import mysql.connector as sql
cnct=sql.connect(host="localhost", user="root", passwd="mysqlpassword", database="patient")
if cnct.is_connected()==False:
    print("Error in connecting MySQL database")
cursor=cnct.cursor()
def First():
    print("\n                                             ------------------------------")
    print("                                        +    WELL CARE HOSPITAL      +")
    print("                                             ------------------------------")
    print("\t \t \t \t \t Making The Impossible, Possible")
    print("\n----------------")
    print("MAIN MENU")
    print("----------------")
    print("1. Doctor Menu")
    print("2. Patient Menu")
    print("3. Exit")
    a=int(input("Enter your choice(1,2,3)= "))
    if a==1:
        Doctor()
    elif a==2:
        Patient()
    elif a==3:
        exit()                                    
    else:
        print("Retry")
        First()
        
def Exit():
    print("Exited Successfully")
    return

def  Doctor():
    def doc_add_more():
        z=input("Do you want to add more?(y/n):")
        if (z=="Y" or z=="y"):
            doc_add()
        elif (z=="NO" or z=="no"):
            Doctor()
        else:
            print("Try again")
            doc_add_more()
            
   #For viewing the entire doctor id 
    
    def doc_id():
        view="select Doctor_id from doctor"
        cursor.execute(view)
        data=cursor.fetchall()
        if data == None:
            doc_add()
        else:
            for row in data:
                print(row)
            
    def  doc_add():
        doc_id()
        b=int(input("Doctor id:"))
        c=input("Name:")
        d=input("Gender(M/F):")
        e=input("Age:")
        f=int(input("Phone number:"))
        g=input("Specialist:")
        h=input("Attending Hours:")
        i=input("Salary:")
        k=input("Address:")
        l=int(input("Aadhar number:"))
        m=input("Certificates Submitted(use only commas to differentiate):")
        insert="INSERT INTO doctor(Doctor_id ,Doctor_name,Gender,Age,Phone_No,Specialist,Attending_Hours,Salary,Address,Aadhar_no,Certificates_Submitted)VALUES({},'{}','{}',{},{},'{}',{},{},'{}',{},'{}')".format(b,c,d,e,f,g,h,i,k,l,m)
        cursor.execute(insert)
        cnct.commit()
        print("\n Contents freshly added!")
        doc_add_more()

    def doc_edit():
        b=int(input("Doctor id to be edited:"))
        c=input("Name:")
        d=input("Gender(M/F):")
        e=input("Age:")
        f=int(input("Phone number:"))
        g=input("Specialist:")
        h=input("Attending Hours:")
        i=input("Salary:")
        k=input("Address:")
        l=int(input("Aadhar number:"))
        m=input("Certificates Submitted(use only commas to differentiate):")
        edit="UPDATE Doctor SET Doctor_name='{}',Gender='{}',Age={},Phone_No={},Specialist='{}',Attending_Hours={},Salary={},Address='{}',Aadhar_no={},Certificates_Submitted= '{}'  WHERE Doctor_id={}". format(c,d,e,f,g,h,i,k,l,m,b)
        cursor.execute(edit)
        cnct.commit()
           
    def doc_view():
        id=input("Do you want to view the entire details?(y/n):")
        if (id=="y" or id=="Y"):
             print("DOCTOR ID , DOCTOR NAME, GENDER, AGE, PHONE NUMBER, SPECIALIST, ATTENDING HOURS, SALARY, ADDRESS, AADHAR NUMBER, CERTIFICATES SUBMITTED")
             view="select * from doctor"
             cursor.execute(view)
             data=cursor.fetchall()
             for row in data:
                 print(row)
        elif(id=="n" or id=="N"):
            a=int(input("Enter the doctor id to be viewed:"))
            ad="SELECT * FROM doctor WHERE Doctor_id={}". format(a)
            cursor.execute(ad)
            data=cursor.fetchall()
            print(data)

#without  patient records

    def doc_delete():
        c=input("Are you sure you want to delete permanently(y/n):")
        if (c=="Y" or c=="y"):
            del1="DELETE FROM doctor WHERE Doctor_id={}". format(b)
            cursor.execute(del1)
            cnct.commit()
            print("Deleted Successfully")
        elif(c=="n" or c=="N"):
            print("Doctor details not deleted")
        else:
            print("Try again")
            doc_delete()
        a=input("Do you want to delete more details(y/n)?")
        if (a=="Y" or a=="y"):
            doc_delete()
        else:
            Doctor() 
   
    #With patient  records
    
    def delete():
        d="SELECT Doctor_id FROM patient "
        cursor.execute(d)
        data=cursor.fetchall()
        for row in data:
            if b in row:
                print("Patient ID, Patient Name,Doctor ID, Doctor Name")
                view="Select Patient_id, Patient_name, Doctor_id, Doctor_name from patient"
                cursor.execute(view)
                data=cursor.fetchall()
                for row in data:
                    print(row)
                a= input("Enter the patient id for deleting the doctor details respectively!")
                st="UPDATE patient SET Doctor_id=null, Doctor_name=null WHERE Patient_id={}". format(a)
                cursor.execute(st)
                cnct.commit()
                doc_delete()
            else:
                print()
    
    #The actual delete function
    
    def main_delete():
        print("  Doctor Name ,Patient Name")
        view="Select   Doctor_name,Patient_name from patient"
        cursor.execute(view)
        data=cursor.fetchall()
        for row in data:
            print(row)
        w=input("Does the doctor to be deleted have patients?(y/n):")
        y=w.capitalize()
        if (y=="Y"):
            delete()
        else:
            doc_delete()
        
    def doc_exit():
        print("\n  ----------You've exited Successfully from Doctor Menu-----------\n")
        First()
     
    """main"""   
    print("\n -----------------------") 
    print("  DOCTOR MENU")
    print("-----------------------")
    print("1.Add ")
    print("2.Edit")
    print("3.View")
    print("4.Delete")
    print("5.Exit")
    a=int(input("Enter your choice(1,2,3,4,5)="))
    if a==1:
       doc_add()
       Doctor()
    elif a==2:
        doc_edit()  
        Doctor()
    elif a==3:
        doc_view()
        Doctor()
    elif a==4:
        b=int(input("Doctor id to be deleted:"))
        main_delete()
        Doctor()
    elif a==5:                  
        doc_exit()
    else:
        print("Retry")
        Doctor()
        First()

def Patient():
    def pat_new():
        view="Select Doctor_id, Doctor_name,Specialist from doctor"
        cursor.execute(view)
        data=cursor.fetchall()
        for row in data:
            print(row)
    
    def pat_add_more():
        z=input("Do you want to add more?(y/n):")
        if (z=="Y" or z=="y"):
            pat_add()
        elif (z=="N" or z=="n"):
            Patient()
        else:
            print("Try again")
            pat_add_more()
            
    def pat_add():
        b=int(input("Patient id:"))
        c=input("Name:")
        d=input("Gender(M/F):")
        e=input("Age:")
        f=int(input("Phone number:"))
        g=input("Blood Group(Format:X positive):")
        h=input("Blood Pressure:")
        i=input("Consultant Fees:")
        j=int(input("Height(in cms):"))
        k=int(input("Weight(in kgs):"))
        l=input("Address:")
        m=input("Problem:")
        n=input("Temperature(in Celsius):")
        o=input("Admitted(y/n):")
        p=input("Ward number:")
        q=input("Room number:")
        s=input("Is the patient visiting for the first time(Yes/No):")
        print("\n The Doctor details: \n")
        pat_new() 
        a1=input("Enter the consulting doctor id:")
        b1=input("Enter the consulting doctor name:")
        insert="INSERT INTO patient(Patient_id ,Patient_name ,Gender,Age ,Phone_Number,Blood_Group,Blood_Pressure,Consultant_fees,Height ,Weight ,Address ,Problem ,Temperature ,Admitted ,Ward_no ,Room_number ,First_timer, Doctor_id, Doctor_name) VALUES({},'{}','{}',{},{},'{}',{},{},{},{},'{}','{}','{}','{}',{},{},'{}',{},'{}')".format(b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,a1,b1)
        cursor.execute(insert)
        cnct.commit()
        print("Contents freshly added!")
        pat_add_more()
    
    def pat_edit():
        b=int(input("Patient id to be edited:"))
        c=input("Name:")
        d=input("Gender(M/F):")
        e=input("Age:")
        f=int(input("Phone number:"))
        g=input("Blood Group(Format:X positive):")
        h=input("Blood Pressure:")
        i=input("Consultant Fees:")
        j=int(input("Height(in cms):"))
        k=int(input("Weight(in kgs):"))
        l=input("Address:")
        m=input("Problem:")
        n=input("Temperature(in Celsius):")
        o=input("Admitted(y/n):")
        p=input("Ward number:")
        q=input("Room number:")
        s=input("Is the patient visiting for the first time(Yes/No):")
        print("\n The Doctor details: \n")
        pat_new() 
        a1=input("Enter the consulting doctor id:")
        b1=input("Enter the consulting doctor name:")
        
        edit="UPDATE patient SET Patient_name='{}' ,Gender='{}',Age={} ,Phone_Number={},Blood_Group='{}',Blood_Pressure={},Consultant_fees={},Height={} ,Weight={} ,Address='{}' ,Problem='{}' ,Temperature={} ,Admitted='{}' ,Ward_no={} ,Room_number={} ,First_timer='{}', Doctor_id={}, Doctor_name='{}' WHERE Patient_id={}".format(c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,s,a1,b1,b)   
        cursor.execute(edit)
        cnct.commit()
    
    def pat_view():
        id=input("Do you want to view the entire details?(y/n):")
        if (id=="y" or id=="Y"):
            print("PATIENT ID ,PATIENT NAME , GENDER, AGE ,PHONE NUMBER, BLOOD GROUP, BLOOD PRESSURE, CONSULTANT FEES, HEIGHT , WEIGHT , ADDRESS , PROBLEM , TEMPERATURE , ADMITTED ,WARD NO , ROOM NUMBER , FIRST TIMER")
            view="select * from patient"
            cursor.execute(view)
            data=cursor.fetchall()
            for row in data:
                print("\n",row)
            print("\n PATIENT NAME, DOCTOR NAME")
            view1="select Patient_name, Doctor_name from patient"
            cursor.execute(view1)
            data1=cursor.fetchall()
            for row1 in data1:
                print("\n",row1)
        elif(id=="n" or id=="N"):
            a=int(input("Enter the patient id to be viewed:"))
            ad="SELECT * FROM patient WHERE Patient_id={}". format(a)
            cursor.execute(ad)
            data=cursor.fetchall()
            print(data)
            print("\n PATIENT NAME, DOCTOR NAME")
            view1="select Patient_name, Doctor_name from patient WHERE Patient_id={}". format(a)
            cursor.execute(view1)
            fix=cursor.fetchall()
            print(fix)

    def pat_delete():
        b=int(input("Patient id to be deleted:"))
        c=input("Are you sure you want to delete permanently(y/n):")
        if (c=="Y" or c=="y"):
            delete="DELETE FROM patient  WHERE Patient_id={}". format(b)             #Not Working
            cursor.execute(delete)
            cnct.commit()
            print("Deleted Successfully")
        elif(c=="n" or c=="N"):
            print("Patient details not deleted")
        else:
            print("Try again")
            pat_delete()  
        a=input("Do you want to delete more details?(y/n)")
        if (a=="Y" or a=="y"):
            pat_delete()
        else:
            Patient()
            
    """mains"""
    print("\n ---------------------")         
    print(" PATIENT MENU")
    print("--------------------- ")    
    print("1.Add ")
    print("2.Edit")
    print("3.View")
    print("4.Delete")
    print("5.Exit")
    a=int(input("Enter your choice(1,2,3,4,5)= "))
    if a==1:
        pat_add()
        Patient()
    elif a==2:
        pat_edit()
        Patient()
    elif a==3:
        pat_view()  
        Patient()
    elif a==4:
         pat_delete()
         Patient()
    elif a==5:
        print("\n ---------------------You've exited from Patient Menu---------------- \n")
        First()
    else:
        print("Retry")
        Patient()
    First()
      
First()
cnct.close()

