from typing import List
from algorithm.model import Share, CSV_FILES_NAME
import csv


# def console_display(title, message: Optional[List or int] = None):
#     print(f"{title} : {message}")
#
#
# def get_best_shares_by_combination(shares, nb_of_shares_combined):
#     console_display(f"\n{nb_of_shares_combined} éléments a combiner")
#     all_combinations = []
#     for combination in combinations(shares, nb_of_shares_combined):
#         all_combinations.append(combination)
#     console_display("nb. de combinaisons", len(all_combinations))
#
#     combinations_below_budget_max = []
#     for every_combination in all_combinations:
#         price_sum = 0
#         for share in every_combination:
#             price_sum = share.get_investment_sum(price_sum)
#         if price_sum <= BUDGET_MAX:
#             combinations_below_budget_max.append(every_combination)
#     console_display("nb. de combinaisons au-dessous du budget", len(combinations_below_budget_max))
#
#     if combinations_below_budget_max:
#         profits_by_combination = []
#         for combination in combinations_below_budget_max:
#             profits = 0
#             for share in combination:
#                 profit = share.get_profit()
#                 profits += profit
#             profits_by_combination.append(profits)
#
#         best_investment = ()
#         best_profit = max(profits_by_combination)
#         for combination_number in range(len(combinations_below_budget_max)):
#             if profits_by_combination[combination_number] == best_profit:
#                 best_investment = combinations_below_budget_max[combination_number]
#
#     else:
#         console_display("Le budget a été dépassé")
#         best_investment = tuple()
#         best_profit = float(0)
#
#     return best_investment, best_profit
#
#
# def get_best_investment(shares):
#     best_shares = []
#     best_profits = []
#     for nb_of_shares in range(len(shares)):
#         best_shares_by_combination = get_best_shares_by_combination(shares, nb_of_shares+1)
#         best_shares.append(best_shares_by_combination[0])
#         best_profits.append(best_shares_by_combination[1])
#
#     best_profit = max(best_profits)
#     best_investment = ()
#     for number_of_share in range(len(best_shares)):
#         if best_profits[number_of_share] == best_profit:
#             best_investment = best_shares[number_of_share]
#
#     console_display("\nLe meilleur profit", best_profit)
#     console_display("Le meilleur investissement", best_investment)


# from algorithms import bruteforce, optimized_v1

# ALGORITHM_PROVIDER: Dict[str, Callable[[List[Share]], Portfolio]] = {
#     'bruteforce': bruteforce.get_best_portfolio,
# }


def load_shares(files_name: List[str]) -> List[Share]:
    shares = []
    for file_name in files_name:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                share = Share.deserialize_csv_file(row)
                shares.append(share)

    return shares


def main(shares_filepath: List[str] = CSV_FILES_NAME):
    shares: List[Share] = load_shares(shares_filepath)
    print("len shares :", len(shares))
    print("shares :", shares)


# def main2(shares_filepath: str = 'resources/dataset1_Python+P7', algorithm: str = 'bruteforce'):
#     shares = load_shares(shares_filepath)
#     algorithm_func: Callable[[List[Share]], Portfolio] = ALGORITHM_PROVIDER[algorithm]
#
#     best_portfolio = algorithm_func(shares)
#
#     nice_print(best_portfolio)


if __name__ == "__main__":
    main()
