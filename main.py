from typing import List
import time
import csv

from algorithm import bruteforce, optimized
from algorithm.model import *
from algorithm.view import TerminalView


ALGORITHM_PROVIDER = {
    'bruteforce': bruteforce.get_best_portfolio,
    'optimized': optimized.get_best_portfolio,
}


def load_shares(files_name: List[str]) -> List[Share]:
    shares = []
    for file_name in files_name:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                share = Share.deserialize_from_csv_file(row)
                if share.price > 0:
                    shares.append(share)

    return shares


def main(shares_filepath: List[str] = CSV_FILE_1, algorithm: str = 'optimized'):
    print("Algorithme en exécution. Attendez un moment, s'il vous plaît...")
    shares: List[Share] = load_shares(shares_filepath)
    algorithm_func = ALGORITHM_PROVIDER[algorithm]

    algorithm_delay_start = time.time()
    final_budget, best_investment, best_portfolio = algorithm_func(shares)
    algorithm_delay_end = time.time()

    view = TerminalView
    view.display_results(algorithm=algorithm,
                         shares=best_portfolio,
                         best_investment=best_investment,
                         final_budget=final_budget)

    print(f"\nTemps d'exécution de l'algorithme '{algorithm}' : "
          f"{round(algorithm_delay_end-algorithm_delay_start, 2)} secondes")


if __name__ == "__main__":
    main()
