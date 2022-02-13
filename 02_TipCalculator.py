#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print( "Welcome to the tip calculator.")
#Get total bill amount
bill_total = float(input("Please enter the total bill amount: "))
#Get tip percentage
tip_total = float(input("What percentage tip will you leave? "))
#Get total amount of people who will split the bill
split_total = int(input("How many people will split the bill? "))
#Calculate total amount per person
amount_per_person = (bill_total / split_total) * (1 + (tip_total / 100))
#Round to 2 decimal places
amount_per_person = round(amount_per_person,2)
#Format to 2 decimal places
amount_per_person = "{:0.2f}".format(amount_per_person)
#Print the final result
print (f"Each person should pay: ${amount_per_person}")
