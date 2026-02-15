print("Bill Split Calculator")
bill_amount = float(input("Enter the total bill amount: "))

tip_percentage = float(input("Enter the tip percentage (e.g., 15): "))

tip_amount = (tip_percentage / 100) * bill_amount

total_bill = bill_amount + tip_amount

print(f"Total (including tip): ${total_bill}")

number_of_people = int(input("Enter the number of people: "))

amount_per_person = total_bill / number_of_people

print(f"Each person pays: ${amount_per_person}")
