from typing import Callable, Dict, List
import time
import csv
from algorithm import bruteforce, optimized
from algorithm.model import *
from algorithm.view import TerminalView


# def create_share_list() -> List:
#     shares: List[Share] = [
#         Share("action-1", 2000, 5),
#         Share("action-2", 3000, 10),
#         Share("action-3", 5000, 15),
#         Share("action-4", 7000, 20),
#         Share("action-5", 6000, 17),
#         Share("action-6", 8000, 25),
#         Share("action-7", 2200, 7),
#         Share("action-8", 2600, 11),
#         Share("action-9", 4800, 13),
#         Share("action-10", 3400, 27),
#         Share("action-11", 4200, 17),
#         Share("action-12", 11000, 9),
#         Share("action-13", 3800, 23),
#         Share("action-14", 1400, 1),
#         Share("action-15", 1800, 3),
#         Share("action-16", 800, 8),
#         Share("action-17", 400, 12),
#         Share("action-18", 1000, 14),
#         Share("action-19", 2400, 21),
#         Share("action-20", 11400, 18),
#     ]
#     return shares


ALGORITHM_PROVIDER: Dict[str, Callable[[List[Share]], Portfolio]] = {
    'bruteforce': bruteforce.get_best_portfolio,
    'optimized': optimized.get_best_portfolio,
}


def load_shares(files_name: List[str]) -> List[Share]:
    shares = []
    for file_name in files_name:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                share = Share.deserialize_csv_file(row)
                if share.price > 0:
                    shares.append(share)

    return shares


def main(shares_filepath: List[str] = CSV_FILE_0, algorithm: str = 'optimized'):
    # shares = create_share_list()
    shares: List[Share] = load_shares(shares_filepath)
    print("len shares :", len(shares))

    algorithm_func: Callable[[List[Share]], Portfolio] = ALGORITHM_PROVIDER[algorithm]

    start = time.time()
    best_investment, best_portfolio = algorithm_func(shares)
    print("best_investment :", best_investment)
    print("best_portfolio :", best_portfolio)
    end = time.time()
    print("algorithm_complexity_time :", end - start)

    view = TerminalView
    view.display_results(algorithm=algorithm, shares=best_portfolio, best_investment=best_investment)


# def main2(shares_filepath: str = 'resources/dataset1_Python+P7', algorithm: str = 'bruteforce'):
#     shares = load_shares(shares_filepath)
#     algorithm_func: Callable[[List[Share]], Portfolio] = ALGORITHM_PROVIDER[algorithm]
#
#     best_portfolio = algorithm_func(shares)
#
#     nice_print(best_portfolio)


if __name__ == "__main__":
    main()
