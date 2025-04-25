import sqlite3

def initialize_database():
    conn = sqlite3.connect("army_solutions.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS solutions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            swordsmen INTEGER,
            bowmen INTEGER,
            horsemen INTEGER,
            power INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_solution(swordsmen, bowmen, horsemen, power):
    initialize_database()
    conn = sqlite3.connect("army_solutions.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO solutions (swordsmen, bowmen, horsemen, power)
        VALUES (?, ?, ?, ?)
    ''', (swordsmen, bowmen, horsemen, power))
    conn.commit()
    conn.close()
