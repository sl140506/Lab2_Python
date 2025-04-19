# program3.py
# Program tworzący prosty słownik na podstawie danych wejściowych

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

people = dict(zip(names, ages))

for name, age in people.items():
    print(f"{name} ma {age} lat.")
