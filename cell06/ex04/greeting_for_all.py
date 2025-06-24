#!/usr/bin/env python3

def greeting(person=None) -> str:
    if person is None:
        print("Hello, Noble Stranger")
    elif not isinstance(person, str):
       print("Error! Not a person.")
    else:
        print("Hello, " + person)

greeting("Alexandires")
greeting("Scription")
greeting()
greeting(42)
