#Ask for N and calculate the sum from 1 to N.
n = int(input("Enter a num for addition frm to N: "))
x = 0
for i in range(1,n+1,1):
    x = x+i
print(x)