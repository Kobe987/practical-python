# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1
extra_payment_start_month = float(
    input("Please input extra payment start month: "))
extra_payment_end_month = float(
    input("Please input extra payment end month: "))
extra_payment = float(input("Please input extra payment: "))
payment_plus_extra = payment+extra_payment
while principal >= payment:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1+rate/12) - payment_plus_extra
        total_paid = total_paid + payment_plus_extra
        month += 1
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        month += 1


print("Total paid", round(total_paid+principal, 2))
print("Months", month)
