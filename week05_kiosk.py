# ISHS CAFFE
# americano 1500,latte 2500
beverage = ["Americano", "Latte"]
prices = ["1500", "2500"]
total_price = 0

while True:
    menu = input("1) Americano 2) Latte 3) End order : ")
    if menu == "3":
        print("Your order had been accepted.")
        break
    elif menu == "1":
        print("You ordered Americano coffee. The price is 1500 won.")
        total_price = total_price + int(prices[0])
    elif menu == "2":
        print("You ordered a cafe latte. The price is 2500 won.")
        total_price = total_price + int(prices[1])
    else:
        print(f"The menu number {menu} you ordered does not exit. Please choose from the menu.")

print(f"The total amount is {total_price} won.")