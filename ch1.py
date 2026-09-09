Name = str(input("Enter Account Holder Name: "))
cr_bal = int(input("Enter the current Balance: "))
with_amt = int(input("Enter the withdraw Amount: "))
re_bal = cr_bal-with_amt

if with_amt <= 0 :
    print("Invalid Withdrawal Amount")
elif with_amt > cr_bal :
    print("Insufficient Balance")
elif with_amt <= cr_bal :
    print("Transaction Successful")
    print(f"Remaining Balance:{re_bal}")