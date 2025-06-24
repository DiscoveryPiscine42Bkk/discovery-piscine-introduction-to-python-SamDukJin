#!/usr/bin/env python3

def advanced_mult():
   i = 0
   while i <= 10:
      print("Table no.", i, end=": ")
      j = 0
      while j <= 10:
         print(i*j, end="  ")
         j += 1
      print(" ")
      i += 1

advanced_mult()
