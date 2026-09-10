#Sum of digits
num = int(input("Enter number: "))
sum = 0
n = 0

while num > 0:
    n = num % 10
    num = num // 10
    sum = sum + n
    print("",n," ",num," ",sum) #for my understanding

print("Sum of digits = ",sum)