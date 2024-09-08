size = input("Enter the size of your house(square ft): ")
size = int(size) # Convert the string into int

square_meter = size / 10.8
# Round a number to given precision value(in this case 2)
square_meter = round(square_meter, 6)
print(f"Your house is {square_meter} Square meter.")

# use f-string to print only given digit after the decimal point
print(f"{square_meter:.2f} Square meter") # it also round the floating point number

# Seperate the number with thousands 
number = 2500000000000.00
print(f"${number:,} USD")

# Multiple input in one line 
a, b, c = input().split()
print(f"{a}, {b}, {c}")