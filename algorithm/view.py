from typing import List
import numpy as np
from matplotlib import pyplot as plt

from algorithm.model import Share


class TerminalView:
    @staticmethod
    def display_results(algorithm: str, shares: List[Share], best_investment: float, final_budget: float):
        print(f"\n ** Résultats de l'algorithme {algorithm} **\n")
        for share in shares:
            print(f"Action : {share.name} | Coût : {share.price} € | Profit : {share.profit} %")

        print(f"\nArgent investi : {final_budget} €")
        print(f"Meilleur bénéfice : {best_investment} €")

    @staticmethod
    def display_chart(operations, delays, label):
        time_x_axis = np.array(delays)
        operations_y_axis = np.array(operations)
        plt.plot(time_x_axis, operations_y_axis, label=label)

        plt.title("Graphique du temps de traitement")
        plt.xlabel("Temps (s)")
        plt.ylabel("Nombre d'opérations")

        plt.legend()
        plt.show()
