#!/usr/bin/env python3

import sys 

new_array = []

if len(sys.argv) > 1:
   for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1) :
      new_array.append(i)
   print(new_array)
else :
   print("No parameter passed.")