# mortgage.py
#
# Exercise 1.8 - Extra payments
# Exercise 1.9 - Making an Extra Payment Calculator
# Exercise 1.10 - Making a table Modify the program to print out a table showing the month, total paid so far, and the remaining principal. 
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
count_number = 1

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
  if ((count_number <= 12) | ((count_number >= extra_payment_start_month) & (count_number <= extra_payment_end_month))):
    principal = principal * (1+rate/12) - (payment + extra_payment)
    total_paid = total_paid + (payment + extra_payment)
    count_number += 1
    print('Month: {}'.format(count_number))
    print('Total paid so far: {}'.format(total_paid))
    print('Remaining Principal: {}'.format(500000 - principal))
  else:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    count_number += 1
    print('Month: {}'.format(count_number))
    print('Total paid so far: {}'.format(total_paid))
    print('Remaining Principal: {}'.format(500000 - principal))
print('Total paid', total_paid)
