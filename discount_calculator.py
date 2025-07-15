purchase_amount = float(input("Enter your purchase amount: "))

if purchase_amount >= 1000:
    discount = 0.1 #10% discount
elif purchase_amount >= 500:
    discount = 0.05 #5% discount
else:
    discount = 0 # No discount

final_price = purchase_amount * (1 - discount)
print("Final price after discount: $" + str(final_price))


score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print("Your grade is:", grade)
