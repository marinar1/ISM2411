# Marina Rodriguez Teixeira
# ISM2411 - Week 10 - Lists and Tuples
#
# Reflection
# 1. The most surprising thing about lists in Python is how many things you can
#    do with just one line, like slicing with [::2] or using negative indexes to
#    get the last item. I also did not expect that lists can change (mutable)
#    but tuples cannot, so Python gives you an error if you try to edit a tuple.
#
# 2. When I worked in marketing and sales at my dad's company, Dentalclean, we
#    kept product and sales information in Excel and a lot of it was done by hand.
#    With a Python list, I could store all the sales numbers and use sum(), max(),
#    min(), or a loop to filter the best days in seconds, instead of copying
#    and calculating everything manually in a spreadsheet.


# EXERCISE 1 - Build the list
print("--- Exercise 1 ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))


# EXERCISE 2 - Index practice
print("\n--- Exercise 2 ---")
print(inventory[0])                      # first item
print(inventory[-1])                     # last item
middle = len(inventory) // 2             # compute middle position
print(inventory[middle])                 # middle item


# EXERCISE 3 - Slicing
print("\n--- Exercise 3 ---")
print(inventory[:3])                     # first three items
print(inventory[-2:])                    # last two items
print(inventory[::2])                    # every other item


# EXERCISE 4 - Modify
print("\n--- Exercise 4 ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# EXERCISE 5 - Tuple comparison
print("\n--- Exercise 5 ---")
coords = (40.7128, -74.0060)             # NYC latitude and longitude
try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples cannot be changed, which is useful for coordinates because a")
    print("location should stay fixed and not be edited by accident.")
print(coords)


# EXERCISE 6 - Average of a list of sales
print("\n--- Exercise 6 ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# EXERCISE 7 - Accumulator pattern
print("\n--- Exercise 7 ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    new_price = round(price * 0.9, 2)    # 10% off, rounded to 2 decimals
    discounted.append(new_price)
print("Original:", prices)
print("Discounted:", discounted)


# EXERCISE 8 - Filter above threshold
print("\n--- Exercise 8 ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
