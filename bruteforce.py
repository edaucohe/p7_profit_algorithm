from itertools import combinations
from typing import List, Optional

from algorithm.model import Share, BUDGET_MAX


def create_share_list() -> List:
    shares: List[Share] = [
        Share("action-1", 20, 0.05),
        Share("action-2", 30, 0.10),
        Share("action-3", 50, 0.15),
        Share("action-4", 70, 0.20),
        Share("action-5", 60, 0.17),
        Share("action-6", 80, 0.25),
        Share("action-7", 22, 0.07),
        Share("action-8", 26, 0.11),
        Share("action-9", 48, 0.13),
        Share("action-10", 34, 0.27),
        Share("action-11", 42, 0.17),
        Share("action-12", 110, 0.09),
        Share("action-13", 38, 0.23),
        Share("action-14", 14, 0.01),
        Share("action-15", 18, 0.03),
        Share("action-16", 8, 0.08),
        Share("action-17", 4, 0.12),
        Share("action-18", 10, 0.14),
        Share("action-19", 24, 0.21),
        Share("action-20", 114, 0.18),
    ]
    return shares


def console_display(title, message: Optional[List or int] = None):
    print(f"{title} : {message}")


def get_best_shares_by_combination(shares, nb_of_shares_combined):
    console_display(f"\n{nb_of_shares_combined} éléments a combiner")
    all_combinations = []
    for combination in combinations(shares, nb_of_shares_combined):
        all_combinations.append(combination)
    console_display("nb. de combinaisons", len(all_combinations))

    combinations_below_budget_max = []
    for every_combination in all_combinations:
        price_sum = 0
        for share in every_combination:
            price_sum = share.get_investment_sum(price_sum)
        if price_sum <= BUDGET_MAX:
            combinations_below_budget_max.append(every_combination)
    console_display("nb. de combinaisons au-dessous du budget", len(combinations_below_budget_max))

    if combinations_below_budget_max:
        profits_by_combination = []
        for combination in combinations_below_budget_max:
            profits = 0
            for share in combination:
                profit = share.get_profit()
                profits += profit
            profits_by_combination.append(profits)

        best_investment = ()
        best_profit = max(profits_by_combination)
        for combination_number in range(len(combinations_below_budget_max)):
            if profits_by_combination[combination_number] == best_profit:
                best_investment = combinations_below_budget_max[combination_number]

    else:
        console_display("Le budget a été dépassé")
        best_investment = tuple()
        best_profit = float(0)

    return best_investment, best_profit


def get_best_investment(shares):
    best_shares = []
    best_profits = []
    for nb_of_shares in range(len(shares)):
        best_shares_by_combination = get_best_shares_by_combination(shares, nb_of_shares+1)
        best_shares.append(best_shares_by_combination[0])
        best_profits.append(best_shares_by_combination[1])

    best_profit = max(best_profits)
    best_investment = ()
    for number_of_share in range(len(best_shares)):
        if best_profits[number_of_share] == best_profit:
            best_investment = best_shares[number_of_share]

    console_display("\nLe meilleur profit", best_profit)
    console_display("Le meilleur investissement", best_investment)


def main():
    shares = create_share_list()
    get_best_investment(shares)


if __name__ == "__main__":
    main()
