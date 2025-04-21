# scripts/analyze.py
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "pomodoro_log.csv")

def load_data():
    """Carga los datos de pomodoro en un DataFrame de pandas."""
    if not os.path.exists(DATA_FILE):
        print(f"Archivo de datos no encontrado: {DATA_FILE}")
        return None
    
    df = pd.read_csv(DATA_FILE)
    df['date'] = pd.to_datetime(df['date'])
    return df

def generate_statistics():
    """Genera estadísticas básicas sobre los registros de pomodoro."""
    df = load_data()
    if df is None or df.empty:
        print("No hay datos para analizar.")
        return
    
    # Estadísticas generales
    total_days = len(df)
    total_time_minutes = df['total_minutes'].sum()
    total_time_hours = total_time_minutes / 60
    avg_daily_minutes = df['total_minutes'].mean()
    
    print(f"\n=== Estadísticas de Pomodoro ===")
    print(f"Días registrados: {total_days}")
    print(f"Tiempo total: {total_time_hours:.1f}h ({total_time_minutes} minutos)")
    print(f"Promedio diario: {avg_daily_minutes:.1f} minutos ({avg_daily_minutes/60:.1f}h)")
    
    # Estadísticas por día de la semana
    weekday_stats = df.groupby('weekday')['total_minutes'].agg(['mean', 'sum', 'count'])
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekday_stats = weekday_stats.reindex(weekday_order)
    
    print("\nPromedio por día de la semana:")
    for day, row in weekday_stats.iterrows():
        if pd.notna(row['mean']):
            print(f"{day}: {row['mean']/60:.1f}h ({row['count']} días)")
    
    # Tendencia semanal
    df['week'] = df['date'].dt.isocalendar().week
    df['year'] = df['date'].dt.isocalendar().year
    df['yearweek'] = df['year'].astype(str) + "-" + df['week'].astype(str)
    weekly_stats = df.groupby('yearweek')['total_minutes'].sum() / 60  # Convertir a horas
    
    print("\nHoras totales por semana:")
    for week, hours in weekly_stats.items():
        print(f"Semana {week}: {hours:.1f}h")
    
    # Visualización
    plt.figure(figsize=(12, 10))
    
    # Gráfico 1: Tiempo por día
    plt.subplot(2, 1, 1)
    plt.bar(df['date'], df['total_minutes'] / 60)
    plt.title('Horas de trabajo por día')
    plt.ylabel('Horas')
    plt.xticks(rotation=45)
    
    # Gráfico 2: Promedio por día de la semana
    plt.subplot(2, 2, 3)
    weekday_means = weekday_stats['mean'] / 60
    weekday_means.dropna().plot(kind='bar')
    plt.title('Promedio de horas por día de la semana')
    plt.ylabel('Horas')
    
    # Gráfico 3: Tendencia semanal
    plt.subplot(2, 2, 4)
    weekly_stats.plot(kind='bar')
    plt.title('Horas totales por semana')
    plt.ylabel('Horas')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    
    # Guardar gráfico
    output_file = os.path.join(os.path.dirname(DATA_FILE), "pomodoro_stats.png")
    plt.savefig(output_file)
    plt.close()
    
    print(f"\nGráfico guardado en: {output_file}")
    
    return df

if __name__ == "__main__":
    generate_statistics()