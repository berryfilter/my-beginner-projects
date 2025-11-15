"""text = "Hello World"""""

"""char_count = {}
for x in text:
    char_count[x] = char_count.get(x, 0) + 1
print(char_count)"""

"""There is an important data class: dictionaries. They always have the structure of (key, value)
.get() is to dictionaries what .append() is to lists. but .get() also says "if it isn't in this dictionary,
 give me a defined value"""

"""favorites = {
    "color": "blue",
    "food": "pizza",
    "animal": "dog",
    "season": "autumn"
}
for category, item in favorites.items():
    print(f"My favorite {category} is {item}")"""

"""When wanting to retrieve the key part, just say the dictionary (here favorites), when you want the
value part, say dictionary.values(), when you want both say dictionary.items()
dictionary[] = value"""

"""dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = {**dict1, **dict2}
print("Combined:", combined)"""

"""movies = {
    "Inception": 8.8,
    "The Matrix": 8.7,
    "Interstellar": 8.6,
    "The Dark Knight": 9.0
}
print(f"Inception rating: {movies['Inception']}")
print(f"Avatar rating: {movies.get('Avatar')}")"""

"""shopping = {
    "apples": 3,
    "bread": 1,
    "milk": 2
}
shopping["eggs"] = 12
shopping["cheese"] = 1

shopping["apples"] = 5
shopping["milk"] += 3

print("Final shopping list:", shopping)"""

kristalle = {
    "Rubin": 50,
    "Saphir": 70,
    "Onyx": 40
}
kristalle["Smaragd"] = 60
kristalle["Onyx"] += 10

print(kristalle["Saphir"])
for kr, value in kristalle.items():
    print(f"{kr}: {value}")










"""def get_planet_name(id):
    # This doesn't work; Fix it!
    name= {

    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune"}
    return name.get(id, name)
print(get_planet_name(1))
"""






































