personen = [
    {"name": "sara", "alter": 33},
    {"name": "John", "alter": 25},
    {"name": "Soraya", "alter": 30},
    {"name": "Helge", "alter": 28}
]
 
erwachsene = list(filter(lambda person: person["alter"] >= 30, personen))
 
for person in erwachsene:
    print(f"{person['name']} ist {person['alter']} Jahre alt")