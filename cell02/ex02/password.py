#!/usr/bin/env python3

password = "Python is awesome"

pass_inp = input("Password: ").strip()

if pass_inp == password :
   print("ACCESS GRANTED")
elif pass_inp != password :
   print("ACCESS DENIED")