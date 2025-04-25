import sqlite3

class ArmyOptimizer:
    def __init__(self):
        self.max_food = 1200
        self.max_wood = 800
        self.max_gold = 600
        self.food = [60, 80, 140]  # swordsmen, bowmen, horsemen
        self.wood = [20, 10, 0]
        self.gold = [0, 40, 100]
        self.power = [70, 95, 230]

    def calculate_optimal_army(self):
        optimal_power = 0
        optimal_solution = (0, 0, 0)  # swordsmen, bowmen, horsemen

        for swordsmen in range(self.max_food // self.food[0] + 1):
            for bowmen in range(self.max_food // self.food[1] + 1):
                for horsemen in range(self.max_food // self.food[2] + 1):
                    total_food = swordsmen * self.food[0] + bowmen * self.food[1] + horsemen * self.food[2]
                    total_wood = swordsmen * self.wood[0] + bowmen * self.wood[1] + horsemen * self.wood[2]
                    total_gold = swordsmen * self.gold[0] + bowmen * self.gold[1] + horsemen * self.gold[2]
                    total_power = swordsmen * self.power[0] + bowmen * self.power[1] + horsemen * self.power[2]

                    if total_food <= self.max_food and total_wood <= self.max_wood and total_gold <= self.max_gold:
                        if total_power > optimal_power:
                            optimal_power = total_power
                            optimal_solution = (swordsmen, bowmen, horsemen)

        return optimal_power, optimal_solution


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
