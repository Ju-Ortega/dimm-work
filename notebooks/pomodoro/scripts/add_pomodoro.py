# scripts/add_pomodoro.py
import os
import csv
import datetime
from datetime import date

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "pomodoro_log.csv")

def ensure_file_exists():
    """Asegura que el archivo CSV exista con los encabezados correctos."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'hours', 'minutes', 'total_minutes', 'weekday', 'notes'])

def add_entry(entry_date=None, hours=0, minutes=0, notes=""):
    """Añade una nueva entrada al registro de pomodoros."""
    ensure_file_exists()
    
    if entry_date is None:
        entry_date = date.today()
    elif isinstance(entry_date, str):
        # Convertir de formato DD/MM/YY a objeto date
        entry_date = datetime.datetime.strptime(entry_date, "%d/%m/%y").date()
    
    total_minutes = hours * 60 + minutes
    weekday = entry_date.strftime("%A")
    
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            entry_date.strftime("%Y-%m-%d"),
            hours,
            minutes,
            total_minutes,
            weekday,
            notes
        ])
    
    print(f"Añadido: {entry_date.strftime('%Y-%m-%d')} - {hours}h {minutes}m ({total_minutes} minutos)")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Añadir registro de pomodoro")
    parser.add_argument("--date", help="Fecha en formato DD/MM/YY (por defecto: hoy)")
    parser.add_argument("--hours", type=int, default=0, help="Horas trabajadas")
    parser.add_argument("--minutes", type=int, default=0, help="Minutos adicionales")
    parser.add_argument("--notes", default="", help="Notas adicionales")
    
    args = parser.parse_args()
    
    add_entry(args.date, args.hours, args.minutes, args.notes)