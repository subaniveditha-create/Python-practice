print("===== BMI Calculator ====")
weight = float(input("Enter your weight in Kg:"))
height = float(input("Enter your height in cm :"))
height_m = height/100
BMI = weight/(height_m**2)
print("Your BMI is:", round(BMI, 2))