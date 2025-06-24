#!/usr/bin/env python3

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(wom_sci):
    for key, details in wom_sci.items():
        print(f"{details['name']} is a great scientist born in {details['date_of_birth']}.")

famous_births(women_scientists)
