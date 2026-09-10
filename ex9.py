#Reverse a number
num = int(input("Enter a number: "))
rev = 0
n = 0

while num > 0:
    n = num % 10
    num = num // 10
    rev = rev*10 + n
    print("",n," ",num," ",rev) #for my understanding

print("Reversed number = ",rev)