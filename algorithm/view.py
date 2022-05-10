from typing import List

from algorithm.model import Share


class TerminalView:
    @staticmethod
    def display_results(algorithm: str, shares: List[Share], best_investment: float):
        print(f" ** Résultats de l'algorithme {algorithm} **\n")
        for share in shares:
            print(f"Action : {share.name} | Coût : {share.price} € | Profit : {share.profit} %")

        print(f"\nMeilleur bénéfice : {best_investment} €")
