size_input = input("How big is your house(in square feet): ")
square_feet = int(size_input)
square_meter = square_feet / 10.8 

# Several ways to print a floating-point number with exactly two decimal places
# round functions 
square_meter = round(square_meter, 2)


# Old style
# square_meter = "%.2f"%square_meter

# # f-string
square_meter = f'{square_meter:.2f}'


message = f'Your house is {square_meter} Square meter.'
print(message)

# Bonus
# Separate thousands 
numbers = 2555553664
print(f'{numbers:,}')