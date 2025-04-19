# program1.py
# Prosty program pobierający dane z API i wypisujący wynik

import requests

response = requests.get("https://api.agify.io?name=John")
if response.status_code == 200:
    data = response.json()
    print(f"Przewidywany wiek dla imienia John: {data['age']}")
else:
    print("Błąd w pobieraniu danych.")
