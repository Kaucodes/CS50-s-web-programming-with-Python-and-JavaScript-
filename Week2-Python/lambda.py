people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]

# Because Python can not compare between two dict..
# def f(person):
#    return person["name"]
# people.sort(key=f)
# OR

people.sort(key=lambda person: person["name"])

print(people)
