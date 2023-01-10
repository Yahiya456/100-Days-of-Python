#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Tip calculator")
bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? ")
split = input("How many people to split the bill? ")
total = float(bill) + ((float(bill) / 100) * (float(tip_percent)))
bill_per_person = round((total / int(split)), 2)
print(f"Each person should pay: ${bill_per_person}")
