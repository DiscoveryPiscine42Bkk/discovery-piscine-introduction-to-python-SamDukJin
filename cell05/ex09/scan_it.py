#!/usr/bin/env python3

import sys

if len(sys.argv) == 3:
   word = sys.argv[1]
   text = sys.argv[2]
   count = text.count(word)
   print(count)
else:
   print("none")
