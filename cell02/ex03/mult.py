#!/usr/bin/env python3

num_inp1 = int(input("Enter first number: "))
num_inp2 = int(input("Enter second number: "))

result = num_inp1 * num_inp2

print(num_inp1, "x", num_inp2, "=", result)

if result > 0 :
   print("The result is positive.")
elif result == 0 :
   print("The result is positive and negative")
elif result < 0 :
   print("The result is negative.")