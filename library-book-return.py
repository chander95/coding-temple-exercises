#library late fees are $1 for 5 days, $2 for 6-10 days, and $5 for over 10 days overdue.
#you must 1. ask the user for the number of days the book is overdue, 2. calcuate the fine based on above criteria, 3. display the fine about to the user

response = input("By how many days are these books overdue? ")
overdue = int(response)

one_day_late = "Your late fee is $1.00 for being " + response + " days late in returning the book/s."
two_days_late = "Your late fee is $2.00 for being " + response + " days late in returning the book/s."
three_days_late = "Your late fee is $5.00 for being " + response + " days late in returning the book/s."

if overdue <= 5:
    print(one_day_late)
elif 6 <= overdue <= 10:
    print(two_days_late)
else:
    print(three_days_late)