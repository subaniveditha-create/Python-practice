#Ask the user for a number and print its multiplication table from 1 to 10.
n = int(input("Multiplication table of which num you want: "))
for i in range (1,11,1):
    print(n,"*",i,"=",i*n)