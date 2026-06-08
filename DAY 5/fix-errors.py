value_str = input("Enter a number: ")
value = int(value_str) # Conversion to integer is required for math!

if value == 10: # Fixed: use double equals '==' for comparison & added trailing colon ':'
  print("Value is ten") # Fixed: Indentation
else:
  print("Value is", value + 5)