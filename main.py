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


def create_chart(algorithm, nb_of_operations, algorithm_delay, view):
    delays = []
    operations = []
    operation = 0
    for nb_of_operation in range(nb_of_operations):
        delays.append(algorithm_delay * nb_of_operation / nb_of_operations)
        operation += 1
        operations.append(operation)

    view.display_chart(operations, delays, algorithm)


def load_shares(files_name: List[str]) -> List[Share]:
    shares = []
    for file_name in files_name:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                share_cts = Share.deserialize_from_csv_file(row)
                if share_cts.price > 0:
                    shares.append(share_cts)

    return shares


def main(shares_filepath: List[str] = CSV_FILE_0, algorithm: str = 'optimized'):
    print("Algorithme en exécution. Attendez un moment, s'il vous plaît...")
    shares: List[Share] = load_shares(shares_filepath)
    algorithm_func = ALGORITHM_PROVIDER[algorithm]

    algorithm_delay_start = time.time()
    final_budget, best_investment, best_portfolio, nb_of_operations = algorithm_func(shares)
    algorithm_delay_end = time.time()

    view = TerminalView
    view.display_results(algorithm, best_portfolio, best_investment, final_budget)

    print(f"\nTemps d'exécution de l'algorithme '{algorithm}' : "
          f"{round(algorithm_delay_end-algorithm_delay_start, 2)} secondes")
    print("Nombre d'opérations : ", nb_of_operations)

    algorithm_delay = algorithm_delay_end-algorithm_delay_start
    create_chart(algorithm, nb_of_operations, algorithm_delay, view)


if __name__ == "__main__":
    main()
