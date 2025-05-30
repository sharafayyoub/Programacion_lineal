from model.resources.food import Food
from model.resources.wood import Wood
from model.resources.gold import Gold
from model.units.swordsmen import Swordsmen
from model.units.horsemen import Horsemen
from model.database_handler import save_solution

class ArmyController:
    def __init__(self):
        self.food = Food(1200)
        self.wood = Wood(800)
        self.gold = Gold(600)
        self.swordsmen = Swordsmen()
        self.horsemen = Horsemen()

    def calculate_optimal_army(self):
        max_food = self.food.amount
        max_wood = self.wood.amount
        max_gold = self.gold.amount

        optimal_power = 0
        optimal_solution = (0, 0, 0)  # swordsmen, bowmen (always 0), horsemen

        for swordsmen in range(max_food // self.swordsmen.food_cost + 1):
            for horsemen in range(max_food // self.horsemen.food_cost + 1):
                total_food = (swordsmen * self.swordsmen.food_cost +
                              horsemen * self.horsemen.food_cost)
                total_wood = (swordsmen * self.swordsmen.wood_cost +
                              horsemen * self.horsemen.wood_cost)
                total_gold = (swordsmen * self.swordsmen.gold_cost +
                              horsemen * self.horsemen.gold_cost)
                total_power = (swordsmen * self.swordsmen.power +
                               horsemen * self.horsemen.power)

                if total_food <= max_food and total_wood <= max_wood and total_gold <= max_gold:
                    if total_power > optimal_power:
                        optimal_power = total_power
                        optimal_solution = (swordsmen, 0, horsemen)  # bowmen is always 0

        return optimal_power, optimal_solution

    def save_solution(self, swordsmen, bowmen, horsemen, power):
        # Guarda la solución usando SQLAlchemy
        save_solution(swordsmen, bowmen, horsemen, power)
