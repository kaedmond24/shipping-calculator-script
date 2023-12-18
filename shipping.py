# Get item weight
weight = input("Enter Item Weight: ")
cost = 0

# Fixed costs
ground_flat_charge = 20.00
ground_premium_flat_charge = 125.00

# Ground Shipping Costs
if weight <= 2:
  cost = (weight * 1.50) + ground_flat_charge
  print(f"Your package weighs {weight}lb.")
  print(f"Total Ground shipping cost is ${round(cost, 2)}")
elif weight > 2 and weight <= 6:
  cost = (weight * 3.00) + ground_flat_charge
  print(f"Your package weighs {weight}lb.")
  print(f"Total Ground shipping cost is ${round(cost, 2)}")
elif weight > 6 and weight <= 10:
  cost = (weight * 4.00) + ground_flat_charge
  print(f"Your package weighs {weight}lb.")
  print(f"Total Ground shipping cost is ${round(cost, 2)}")
else:
  cost = (weight * 4.75) + ground_flat_charge
  print(f"Your package weighs {weight}lb.")
  print(f"Total Ground shipping cost is ${round(cost, 2)}")

# Calculate cost to add premium shipping
print("----- ----- ----- ----- -----")
print(f"Add Ground Shipping Premium for ${ground_premium_flat_charge}")
print(f"Total with Premium ${round((cost + ground_premium_flat_charge), 2)}")
print("----- ----- ----- ----- -----")

# Drone Shipping
if weight <= 2:
  cost = weight * 4.50
  print(f"Total Drone shipping cost is ${cost}")
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
  print(f"Total Drone shipping cost is ${round(cost, 2)}")
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
  print(f"Total Drone shipping cost is ${round(cost, 2)}")
else:
  cost = weight * 14.25
  print(f"Total Drone shipping cost is ${round(cost, 2)}")
