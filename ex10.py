#Find the largest number
#Ask the user how many numbers they want to enter
num = int(input("How many numbers? "))
large = 0

for i in range(1 , num+1 , 1):
    n = int(input("Enter number : "))
    if n > large:
        large = n
    #print ("current num",n,"large num",large) #for understanding
print("The Largest num =",large)
