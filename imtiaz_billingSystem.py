menu = {
    "milk": 220,
    "eggs": 150,
    "water": 70,
    "bread": 100,
    "tea": 800
}

cart = {}
ledger = {} 


print(" Available Items Menu:")
print(f"{'Item':<15}{'Price'}")
for item, price in menu.items():
    print(f"{item:<15}{price:<3} PKR")

customer_name = input("\nEnter customer name: ").strip().title()

print("\nEnter items and quantity (e.g. bread 2). Press Ctrl+Z (Windows) or Ctrl+D (Linux/mac) to finish.\n")

try:
    while True:
        item = input("Item: ").lower()

        parts = item.split()
        item = parts[0]
        quantity = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1

        if item in menu:
            if item in cart:
                cart[item]["quantity"] += quantity
                cart[item]["total_price"] += menu[item] * quantity
            else:
                cart[item] = {
                    "quantity": quantity,
                    "unit_price": menu[item],
                    "total_price": menu[item] * quantity
                }
        else:
            print("Item not in menu. Ignored.")

except EOFError:
    print("\n Input finished.\n")


if cart:
    print(f"-------- FINAL BILL for {customer_name} --------")
    total = 0
    print(f"{'Item':<15}{'Qty':<5}{'Unit':<5}{'Total'}")
    for item, details in cart.items():
        print(f"{item:<15}{details['quantity']:<5}{details['unit_price']:<5}{details['total_price']:<5}")
        total += details['total_price']

    print(f"\nTotal Amount Due: {total} PKR")

    while True:
        try:
            paid = float(input("Enter amount customer is paying now: "))
            break
        except ValueError:
            print("Please enter a valid number.")

   
    if paid == total:
        print("Payment complete. No balance or dues.")
    elif paid > total:
        print(f"Payment complete. Return balance: {paid - total:.2f} PKR")
    else:
        due = total - paid
        ledger[customer_name] = due
        

    if ledger:
        print("\n-------- Customer Ledger --------")
        for name, due in ledger.items():
            print(f"{name}: {due:.2f} PKR Due")
else:
    print("Cart is empty. No items purchased.")
