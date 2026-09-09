yr = int(input("Enter year: "))
if yr%400 == 0 :
    print("Leap year")
elif yr%100 == 0 :
        print("Not a leap year")
elif yr%4 == 0 :
        print("Leap year")
else :
    print("Not a leap year")