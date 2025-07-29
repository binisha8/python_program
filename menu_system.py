menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Momo': 120,
    'Samosa': 25,
    'Milk Tea': 30,
}

print("Welcome to My Restaurant")
print("------ MENU ------")
for item , price in menu.items():
    print(f"{item}: Rs {price}")

order_total=0
order_list=[]


while True:
    item=input("\nEnter the name of the item you want to order: ").title()

    if item in menu:
          quantity=int(input(f"How many {item}s do you want?"))
          cost=menu[item]*quantity
          order_total += cost
          order_list.append((item,quantity,cost))
          print(f"{quantity} {item}(s) added to your order.")

    else:
         print("Item not available")
    
    another_order= input("Do you want to add another item?(Yes/No):").lower()
    if another_order !="yes":
         break
    

print("\n------BILL------")
for item,quantity,price in order_list:
     print(f"{item}*{quantity} = Rs {price}")
print(f"Total Amount to Pay : Rs{order_total}")
