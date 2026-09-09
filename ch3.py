name = input("Enter Student Name: ")
m1 = int(input("Enter English mark:"))
m2 = int(input("Enter Tamil mark:"))
m3 = int(input("Enter science mark:"))
m4 = int(input("Enter Maths mark:"))
m5 = int(input("Enter Scocial mark:"))
grade =""
total = m1+m2+m3+m3+m4+m5
avg = total/5
status = ""
for i in (m1,m2,m3,m4,m5,avg):
    if i >= 90:
        grade = "Grade A"       
    elif i >= 80:
        grade = "Grade B"        
    elif i >= 70:
        grade = "Grade C"        
    elif i >= 60:
        grade = "Grade D"       
    elif i<60:
        grade = "Fail"
    print(f"{i} {grade}")

if m1<35 or m2<35 or m3<35 or m4<35 or m5<35:
    status = "Fail"
else :
    status = "Pass"    
print("********Report Card********")
print("Student Name:",name)
print("Subject Marks:",m1,m2,m3,m4,m5)
print("Toatl :",total)
print("Average :",avg)
print("Grad :",grade)
print("Status :",status)