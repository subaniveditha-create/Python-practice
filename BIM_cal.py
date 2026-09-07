print("====== BMI Calculator ======")

weight = float(input("Enter your weight in Kg: "))
height_cm = float(input("Enter your height in cm: "))

# Convert height from cm to meters
height_m = height_cm / 100

# Calculate BMI
bmi = weight / (height_m ** 2)

print("\nYour BMI is:", round(bmi, 2))

# Find BMI category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Healthy Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\nKeep working towards your fitness goal! ")