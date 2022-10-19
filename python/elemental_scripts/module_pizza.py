def make_pizza (size, *toppings):
	''' Summarize the pizza toppings'''
	print(f"\nMaking a {size}-inch pizza with this toppings:")
	for topping in toppings:
		print(f"- {topping}")

def print_price(size):
	''' Prints the price based on size'''
	print(f"Price: {size*3}")

