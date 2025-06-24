#!/usr/bin/env python3

num_inp = input("Give me a number: ")

try:
   num = float(num_inp)
   if num - int(num) > 0:
      print(int(num) + 1)
   else:
      print(int(num))
except ValueError:
   print("Invalid input.")

