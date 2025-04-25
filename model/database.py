import sqlite3

class Database:
    def __init__(self, db_name="army_solutions.db"):
        self.db_name = db_name
        self.initialize_database()

    def initialize_database(self):
        conn = sqlite3.connect(self.db_name)
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

    def save_solution(self, swordsmen, bowmen, horsemen, power):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO solutions (swordsmen, bowmen, horsemen, power)
            VALUES (?, ?, ?, ?)
        ''', (swordsmen, bowmen, horsemen, power))
        conn.commit()
        conn.close()
