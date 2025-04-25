import tkinter as tk
from controller.army_controller import ArmyController

class ArmyApp:
    def __init__(self):
        self.controller = ArmyController()
        self.root = tk.Tk()
        self.root.title("Army Optimizer")

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        tk.Label(self.root, text="Army Optimizer", font=("Arial", 16)).pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        tk.Button(self.root, text="Calculate Optimal Army", command=self.calculate).pack(pady=10)

    def calculate(self):
        # Calcula el ejército óptimo
        optimal_power, (swordsmen, bowmen, horsemen) = self.controller.calculate_optimal_army()
        # Guarda la solución en la base de datos
        self.controller.save_solution(swordsmen, bowmen, horsemen, optimal_power)
        # Muestra el resultado en la interfaz gráfica
        self.result_label.config(
            text=f"Optimal Power: {optimal_power}\n"
                 f"Swordsmen: {swordsmen}, Bowmen: {bowmen}, Horsemen: {horsemen}"
        )
