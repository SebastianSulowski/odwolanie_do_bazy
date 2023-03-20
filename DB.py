import sqlite3
import csv

stations_file = 'clean_stations.csv'
measure_file = 'clean_measure.csv'

db_file = 'my_database.db'


conn = sqlite3.connect(db_file)
c = conn.cursor()

c.execute('''CREATE TABLE stations
             (station_id INTEGER PRIMARY KEY,
              station_name TEXT,
              latitude REAL,
              longitude REAL)''')


with open(stations_file, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # pomiń nagłówek
    for row in reader:
        c.execute('INSERT INTO stations VALUES (?,?,?,?)', row)


c.execute('''CREATE TABLE measurements
             (station_id INTEGER,
              date TEXT,
              pollutant TEXT,
              value REAL,
              unit TEXT)''')


with open(measure_file, newline='') as f:
    reader = csv.reader(f)
    next(reader)  # pomiń nagłówek
    for row in reader:
        c.execute('INSERT INTO measurements VALUES (?,?,?,?,?)', row)

conn.commit()

print("Tabela stations:")
print(c.execute("SELECT * FROM stations LIMIT 5").fetchall())

print("Tabela measurements:")
print(c.execute("SELECT * FROM measurements LIMIT 5").fetchall())

conn.close()
