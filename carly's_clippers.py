# Data for Carly's Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew",
              "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# --- 1. Average haircut price ---
total_price = sum(prices)                     # Sum of all haircut prices
average_price = total_price / len(prices)     # Mean price
print("Average Haircut Price:", average_price)

# --- 2. New prices (each reduced by $5) ---
new_prices = [price - 5 for price in prices]
print("New Prices:", new_prices)

# --- 3. Total revenue for last week ---
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)

# --- 4. Average daily revenue ---
average_daily_revenue = total_revenue / 7
print("Average Daily Revenue:", average_daily_revenue)

# --- 5. Haircuts under $30 (after price cut) ---
cuts_under_30 = [
    hairstyles[i] for i in range(len(new_prices))
    if new_prices[i] < 30
]
print("Cuts Under $30:", cuts_under_30)
