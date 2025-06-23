num_inp = input("Give me a number: ")

try:
   if float(num_inp).is_integer():
      print("This number is an integer.")
   else:
      print("This number is a float.")
except ValueError:
   print("Invalid input.")

