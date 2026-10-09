# Global variable
cups_sold = 200

def update_sales():
    # Local variable shadows the global variable
    cups_sold = 250

    print("Local cups_sold:", cups_sold)

    # Accessing the global variable
    print("Global cups_sold:", globals()['cups_sold'])
    

# Function call
update_sales()
# Daily coffee orders
daily_orders = [120, 150, 180, 90, 200]

# Calculate daily revenue using map and lambda
daily_revenue = list(map(lambda cups: cups * 5, daily_orders))

# Find highest sales using max()
highest_sales = max(daily_orders)

# Display results
print("Daily Orders:", daily_orders)
print("Daily Revenue:", daily_revenue)
print("Highest Daily Sales:", highest_sales)

