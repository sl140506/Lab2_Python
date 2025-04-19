# app.py
# Program z dwoma zmiennymi i regułą decyzyjną

def decyzja(temp, wilgotnosc):
    if temp > 25 and wilgotnosc < 60:
        return "Włącz klimatyzację"
    elif temp < 18:
        return "Włącz ogrzewanie"
    else:
        return "Warunki są komfortowe"

# Przykładowe wywołania
print(decyzja(27, 50))  # Włącz klimatyzację
print(decyzja(16, 70))  # Włącz ogrzewanie
print(decyzja(22, 65))  # Warunki są komfortowe
