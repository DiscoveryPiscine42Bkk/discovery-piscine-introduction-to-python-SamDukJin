#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

print("Original array: ", original_array)
for i in range(0, len(original_array)):
   if original_array[i] > 5:
      new_array.add(original_array[i] + 2)

print("New array: ", new_array)

