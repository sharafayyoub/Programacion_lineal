class ArmyView:
    @staticmethod
    def display_solution(optimal_power, swordsmen, bowmen, horsemen):
        print('================= Solution =================')
        print(f'Optimal power = {optimal_power} 💪power')
        print('Army:')
        print(f' - 🗡️Swordsmen = {swordsmen}')
        print(f' - 🏹Bowmen = {bowmen}')
        print(f' - 🐎Horsemen = {horsemen}')
