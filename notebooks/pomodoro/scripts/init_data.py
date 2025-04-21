# scripts/init_data.py
from add_pomodoro import add_entry

# Datos existentes
data = [
    ("01/04/25", 5, 40),
    ("02/04/25", 4, 10),
    ("03/04/25", 5, 30),
    ("04/04/25", 8, 0),
    ("07/04/25", 6, 20),
    ("08/04/25", 6, 40),
    ("09/04/25", 3, 0),
    ("10/04/25", 6, 40),
    ("11/04/25", 2, 40),
    ("14/04/25", 3, 20),
    ("15/04/25", 4, 10),
    ("16/04/25", 5, 50)
]

for date, hours, minutes in data:
    add_entry(date, hours, minutes)

print("Datos inicializados correctamente.")