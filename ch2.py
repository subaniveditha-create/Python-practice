name = input("Enter Employee Name: ")
bas_salary = int(input("Enter Basic Salary: "))
hra = bas_salary*.2
da = bas_salary*.1
bonus = bas_salary*.05
tax = bas_salary*.08
gross_sal = bas_salary + hra + da + bonus
net_sal = gross_sal - tax

Income_catogory = " "
if net_sal>= 100000 :
    Income_catogory ="High income"
elif 50000<=net_sal<100000 :
    Income_catogory ="Medium income"
else :
    Income_catogory ="Low income"


print("\n ====================================")
print("\n            Salary Slip              ")
print("\n ====================================")
print(f"Name :{name}")
print(f"Income Catogory ={Income_catogory}")
print(f"Net salary ({net_sal}) = Gross Salary ({gross_sal}) - Deduction ({tax})")
print("\n ====================================")

print("Salary breakdown")
print("\n ")
print("Basic Salary =" ,bas_salary)
print("HRA =" ,hra)
print("DA =" ,da)
print("Bonus =" ,bonus)
print("\n ")
print("Gross Salary =",gross_sal)
print("====================================")
print("Deduction")
print("\n ")
print("TAX = ",tax)
print("\n ")
print("Net Salary = ",net_sal)