class CreditCard():
    def __init__(self,number,holder,balance):
        self.number=number
        self.holder=holder
        self.balance=balance
    def validate(self) :
        reversed_number = str(self.number)[::-1] 
        card = [
        int(digit)*2 - 9 if i % 2 == 1 and int(digit)*2 > 9
        else int(digit)*2 if i % 2 == 1
        else int(digit)
        for i, digit in enumerate(reversed_number)
        ]
        if sum(card) % 10 == 0:
            print("Card is Valid !")
            return True
        else:
            print("Card is Invalid !")
            return False


    def Charge_bill(self,bill):
        if self.balance>bill:
            self.balance-=bill
            print(f"Your Balance is now : {self.balance} PKR")
        else:
            print("Not Sufficient Balance !")

def bill_amount(cart):
    price=0
    for item, quantity in cart.items():
        price += quantity*menu[item]                
    return price
bank_db = {
    "4111111111111111": CreditCard("4111111111111111", "Sara", 10000),
    "5500000000000004": CreditCard("5500000000000004", "Ali", 15000),
    "340000000000009":  CreditCard("340000000000009", "hashim", 15000),
    "6011000000000004": CreditCard("6011000000000004", "saim", 25000)
}
menu={
    "apple":150,
    "banana":100,
    "cherry":200,
    "date":250,
    "mango":300,
    "milk":220,
    "eggs":170,
    "bread":120,
    "cheese":350,
    "yogurt":180,   
    "orange":130,
    "grapes":160,
    "watermelon":280,
    "kiwi":240,
}

print("Welcome to the Shopping Cart!")
print("The following items are in their normal units like kg, liter, etc.")
print(" ========== MENU ========== ")
print(f"{'Item':<10} | {'Price':<8}")
print("-" * 25)
for items,price in menu.items():
    quantity = menu[items]
    print(f"{items:<10} | {price:<8}")
user_cart={}    


while True:
    item = input("Enter the item you want to buy (or 'exit' to quit): ").strip().lower()
    if item=="exit" and user_cart:
        print("Thank you for shopping with us!")
        while True:
        
            try:
                card_no = input("Enter Your Card Number: ").strip()
                card = bank_db[card_no]  
                if card.validate(): 
                    spent = bill_amount(user_cart)
                    print("Your Cart : ")
                    print(f"{'Item':<10} | {'Quantity':<8}| {'Unit Price':<8}   | {'Total Price':<8}")
                    print("-" * 50)
                    for items,quantity in user_cart.items():
                        price=menu[items]
                        total_price = quantity * price
                        print(f"{items:<10} | {quantity:<8}| {price:<8}     | {total_price:<8}")
                    print(f"Your total bill: {spent} PKR")
                    card.Charge_bill(spent)

                    break  
                else:
                    continue
            except KeyError:
                print("Card not found in database. Please try again.")  

            
        break
    elif item=="exit" and not user_cart:
        print("Thank you ! Your cart is empty.")
        break   
    else:
         quantity = int(input("Enter the quantity: "))

    if item in user_cart:
        user_cart[item]+=quantity
        print(f"{item} added to your cart")
    elif item not in user_cart and item in menu:
        user_cart[item] = quantity
        print(f"{item} added to your cart")
    elif item not in menu:    
        print(f"Sorry, {item} is not available in the menu") 
        continue
