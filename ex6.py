#Ask for a number and calculate its factorial.
n = int(input("Enter a num for its factorial: "))
x = 1
for i in range(1,n+1,1):
    x = x*i
    print(x)
print(f"factorial of {n} is ",x)