
print('Welcome to the tip calculator.\n')

# getting how much the bill cost 
bill = input('How much was the bill? ')

# how many people are contributing to the bill
people = input('How many are you? ')

# how much tip is the waiter getting
tip = input('how much are you tipping? 15%, 25%, or 30%: ')

# converting the bill cost into float
bill_as_float = float(bill)

# converting number of people into integer
people_as_int = int(people)

# dividing the bill by the number of people
cost = bill_as_float / people_as_int

# dividing the tip input by 100 to get percentage 
tip_as_float = float(tip)/100

# multiplying the cost by tip percentage 
total_as_float = cost * tip_as_float

# getting total cost after adding tip
billTotal = cost + total_as_float

print('Each person should contribute: R',billTotal)