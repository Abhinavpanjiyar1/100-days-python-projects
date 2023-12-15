print("welcome to the tip calculator.")
bill = int(input("what was the total bill? $"))
tip = int(input("what percent tip would you like to give? 10,12 or 15"))
people = int(input("how many people to split the bill?"))
tip_percent = tip/100
total_bill = tip_percent*bill+bill
bill_per_person = total_bill/people
print(f"bill person is {bill_per_person}")
