# program2.py
# Program z obsługą błędów przy żądaniu do API

import requests

try:
    response = requests.get("https://api.genderize.io?name=Anna")
    response.raise_for_status()
    data = response.json()
    print(f"Płeć dla imienia Anna: {data['gender']}")
except requests.RequestException as e:
    print(f"Wystąpił błąd: {e}")
