num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
num3 = int(input("Enter 3rd num: "))
if num1 == num2 == num3 :
     print("all numbers are equal")
elif num1>num2 and num1>num3 :
    print("The largest num is: ",num1)
elif num2>num1 and num2>num3 :
     print("The largest num is: ",num2)
else :
     print("The largest num is: ",num3)