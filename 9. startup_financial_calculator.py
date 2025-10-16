# Description:
# you're an entrepreneur with a brilliant company idea for a new software-as-a-service (SaaS) startup:
# Before pitching to investors you need to create a financial model to project your costs, revenue,
# and break-even point. You're task is to complete a python script to calculate these crucial financial
# metrics

# 1. Calculate total startup cost: Sum up the individual startup costs (development, marketing,
# equipment) to get the total initial investment needed.

# 2. Project monthly revenue: Calculate the expected monthly revenues bases on the number users in
# each subscription tier and their respective prices.

# 3. Calculate Monthly operating costs: Sum up all the monthly recurring costs to determine your total
# monthly operating expenses

# 4. Determine Monthly Profit: Subtract the monthly operating costs from the monthly revenue to find
# out how profit (or loss) you're making each month

# 5. Estimate time to break even: Calculate how many month it will take to recover your initial
# investment based on monthly profit

# 6. Implement the sensitivity analysis: Create code that adjust the number of users in each tier
# and re-calculate all financial metrics. This will help you understand how changes in user
# aquisition affect your projects.

# 7. Format and Display results: Using f string to format the results, display the currency value
# with commas, and two decimal places, and rounding the break even time to one decimal place.


# Startup Costs
dev_cost = 50000
marketing_cost = 20000
equipment_cost = 10000

#subscription tiers
basic_tier_price= 9.99
pro_tier_price = 19.99
basic_tier_users = 1000
pro_tier_users = 500

# Monthly operating costs
server_cost = 1000
support_cost = 5000
misc_cost = 2000

# TODO: Calculate total startup cost
total_startup_cost = dev_cost + marketing_cost + equipment_cost

# TODO: Calculate monthly revenue
monthly_revenue = (basic_tier_price * basic_tier_users) + (pro_tier_price * pro_tier_users)

# TODO: Calculate monthly operation cost
monthly_cost = server_cost + support_cost + misc_cost

# TODO: Calculate monthly profit
monthly_profit = monthly_revenue - monthly_cost

# TODO: Calculate months to break even
months_to_break_even = total_startup_cost / monthly_profit

# TODO: Display results using formatted strings
print("Financial Projects:")
print(f"Print Total Startup Cost: {total_startup_cost:,.2f}")
print(f"Monthly Revenue: {monthly_revenue:,.2f}")
print(f"Monthly Profit: {monthly_profit:,.2f}")
print(f"Months to Break Even: {months_to_break_even:,.1f}")

