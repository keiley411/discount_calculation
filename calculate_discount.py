# calculating the price for a given discount of 20%
# define vaiables
price = float(input("Enter the price: "))
discount_percent = float(input(" Enter the percentage: "))

# calculate discount amount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        new_price = price - discount_amount
        print(f"Discount is {discount_amount} and new price is {new_price}")

    else:
        print(f"The percentage is {discount_percent}% and price is {price}")

calculate_discount(price, discount_percent)

