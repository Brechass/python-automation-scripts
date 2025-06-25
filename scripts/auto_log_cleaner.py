# scripts/auto_log_cleaner.py

import os
import time

def clean_logs(log_dir="/var/log", days_old=7):
    now = time.time()
    deleted = []

    print(f"\nBuscando archivos en {log_dir} con más de {days_old} días...\n")

    for root, dirs, files in os.walk(log_dir):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                file_mtime = os.path.getmtime(filepath)
                if now - file_mtime > days_old * 86400:  # 86400 = segundos por día
                    os.remove(filepath)
                    deleted.append(filepath)
            except Exception as e:
                print(f" No se pudo borrar {filepath}: {e}")

    print(f"\n Se eliminaron {len(deleted)} archivos:")
    for path in deleted:
        print(f"  - {path}")

if __name__ == "__main__":
    dias = input("¿Cuántos días de antigüedad deben tener los logs para borrarlos?: ")
    try:
        dias = int(dias)
        clean_logs(days_old=dias)
    except ValueError:
        print("Introduce un número válido.")
