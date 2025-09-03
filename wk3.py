# Assignment.py/Wk3.py
# This function calculates the final price after applying a discount based on the original price and discount percentage provided by the user.
# If the discount is 20% or higher, the discount is applied; otherwise, the original price is returned.
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))
# Calculate the final price
print(f"final price = {calculate_discount(price,discount_percent)}")