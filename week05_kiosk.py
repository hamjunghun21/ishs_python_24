# ISHS CAFFE
# americano 1500,latte 2500
beverage = ["Americano", "Latte", "Iced tea"]
prices = [1500, 2500, 2300]
quantity = [0, 0, 0]
total_price = 0

while True:
    menu = input("1) Americano 2) Latte 3) Iced tea 4) End order : ")
    if menu == "4":
        print("Your order had been accepted.")
        break
    elif menu == "1":
        print("You ordered Americano coffee. The price is 1500 won.")
        total_price = total_price + prices[0]
        quantity[0] = quantity[0] + 1
    elif menu == "2":
        print("You ordered a cafe latte. The price is 2500 won.")
        total_price = total_price + prices[1]
        quantity[1] = quantity[1] + 1
    elif menu == "3":
        print("You ordered a iced tea. The price is 2300 won.")
        total_price = total_price + prices[2]
        quantity[2] = quantity[2] + 1
    else:
        print(f"The menu number {menu} you ordered does not exit. Please choose from the menu.")

if quantity[0] != 0:
    print(f"{beverage[0]}\n\t{prices[0]} x{quantity[0]}\t{prices[0]*quantity[0]}")
if quantity[1] != 0:
    print(f"{beverage[1]}\n\t{prices[1]} x{quantity[1]}\t{prices[1]*quantity[1]}")
if quantity[2] != 0:
    print(f"{beverage[2]}\n\t{prices[2]} x{quantity[2]}\t{prices[2]*quantity[2]}")
print(f"The total amount is {total_price} won.")