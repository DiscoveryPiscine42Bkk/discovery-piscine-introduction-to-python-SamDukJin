#!/usr/bin/env python3

person = {
   "James" : "Wilson",
   "Michale" : "Jackson",
   "John" : "Wick",
   "Steve" : "Jobs"
}


def array_of_names(dictofperson):
   full_names = []
   for first, last in dictofperson.items():
      full_names.append(f"{first.capitalize()} {last.capitalize()}")
   return full_names


print(array_of_names(person))