from model import ArmyOptimizer, Database
from view import ArmyView

class ArmyController:
    def __init__(self):
        self.optimizer = ArmyOptimizer()
        self.database = Database()
        self.view = ArmyView()

    def run(self):
        optimal_power, (swordsmen, bowmen, horsemen) = self.optimizer.calculate_optimal_army()
        self.view.display_solution(optimal_power, swordsmen, bowmen, horsemen)
        self.database.save_solution(swordsmen, bowmen, horsemen, optimal_power)
