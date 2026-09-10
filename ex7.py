#Count digits
num = int(input("Enter number: "))
count = 0

while num > 0:
    num = num // 10
    count = count + 1
    print("",num,"        ",count) #for my understanding

print("Number of digits = ",count)