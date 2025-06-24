#!/usr/bin/env python3

import sys

def downcase_all(word) -> str:
   return word.lower()
if len(sys.argv) > 1:
   for arg in (sys.argv) :
      print(downcase_all(arg))
else :
   print("None.")
