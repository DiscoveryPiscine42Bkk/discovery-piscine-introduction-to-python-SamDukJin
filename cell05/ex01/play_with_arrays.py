#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []

print("Original array: ", original_array)
for i in range(0, len(original_array)) :
   new_array.append(original_array[i] + 2)

print("New array: ", new_array)
