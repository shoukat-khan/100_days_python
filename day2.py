print("welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
#or we can use the following code 1+tip/100



total_tip_amount = total_bill * (tip / 100)
total_bill = total_bill + total_tip_amount
bill_per_person = total_bill / people

print(f"Each person should pay: ${bill_per_person:.2f}")