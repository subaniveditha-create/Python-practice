Name = str(input("Enter your name: "))
Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter your weight in kg: "))
BMI = Weight/(Height**2)
print("bmi is ", BMI)
if BMI < 18.5 :
        print(Name, "is underweight")
elif 18.5<= BMI <24.9 :
    print(Name, "is normal")
elif 25<= BMI <29.9 :
    print(Name, "is Overweight")
else :
    print(Name, "is Obese")