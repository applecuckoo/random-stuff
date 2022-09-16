# AtlantaPizza.py

# Ask the person for how many pizzas they want.
number_of_pizzas = eval(input("How many pizzas do you want? "))

# Ask for the menu cost of each pizza.
cost_per_pizza = eval(input("How much does each pizza cost? "))

# Calculate the total cost of the pizzas as our subtotal.
subtotal = number_of_pizzas * cost_per_pizza

# Calculate the sales tax owed, at 8 percent of the subtotal.
tax_rate = 0.08     # Store 8% as the decimal value 0.08
sales_tax = subtotal * tax_rate

# Add the sales tax to the subtotal for the final total.
total = subtotal + sales_tax

# Show the user the total amount due, including tax.
print("The total cost is $", total)
print("This includes $", subtotal, "for the pizza/s and")
print("$", sales_tax, "in sales tax.")
