#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
   for arg in sys.argv[1:]:
      if not arg.endswith("ism"):
         print(arg + "ism")
else :
   print("No parameter passed.")

