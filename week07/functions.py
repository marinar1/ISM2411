#--- Exercise  1 ---

#Define calculate tax function

def calculate_tax(price, rate):
    return price * rate
#Calling the functionn

tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax (250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}") #7.00
print(f"Tax on $250 at 8%: ${tax2:.2f} ") #20.00

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
    
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")

# --- Exercise 3 ---

# Manually first , than factor it 

discounted = apply_discount ( 200, "gold")
tax = calculate_tax (discounted,0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# --- Exercise 4 ---

orders =[(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # Bug 2 (line 63): "=" replaced the total each time; "+=" adds each sale
print(f"Total: ${total}")

count = 0
for sale in sales: # Bug 1 (line 67): the for loop was missing ":" at the end
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Bug 3 (line 72): "<=" went one step too far (index 5 doesn't exist), "<" stops at 4
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100
def double_it():
    x= 999
    return x * 2

print(x)
print(double_it())
print(x)