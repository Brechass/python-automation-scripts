# python-automation-scripts

Este repositorio contiene scripts útiles de automatización desarrollados con Python.

Todos ellos están pensados para tareas reales que pueden servir en entornos de administración de sistemas, scraping de datos o ciberseguridad básica.

## Scripts incluidos:

| Script                  | Descripción |
|------------------------|-------------|
| scrape_news.py         | Scraper que extrae titulares de El País |
| auto_log_cleaner.py    | Borra logs antiguos en `/var/log` según antigüedad |
| disk_usage_report.py   | Muestra el uso de disco por directorio (Analiza cuánto ocupa cada carpeta dentro de una ruta), útil para admins |
| check_open_ports.py    | Escanea puertos abiertos en una IP (TCP) [Con barra de progreso) |

## Requisitos

Instala las dependencias:

```bash
pip install -r requirements.txt
