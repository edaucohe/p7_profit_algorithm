from itertools import combinations
from typing import List

from algorithm.model import BUDGET_MAX, Share


def get_best_shares_by_combination(shares: List[Share], nb_of_shares_combined: int):
    all_combinations = []
    for combination in combinations(shares, nb_of_shares_combined):
        all_combinations.append(combination)
    print("nb. de combinaisons : ", len(all_combinations))

    combinations_below_budget_max = []
    for every_combination in all_combinations:
        price_sum = 0
        for share in every_combination:
            price_sum = share.get_investment_sum(price_sum)
        if price_sum <= BUDGET_MAX*100:
            combinations_below_budget_max.append(every_combination)
    print("nb. de combinaisons au-dessous du budget : ", len(combinations_below_budget_max))

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
        print("Le budget a été dépassé")
        best_investment = tuple()
        best_profit = float(0)

    return best_investment, best_profit


def get_best_portfolio(shares: List[Share]):
    best_shares = []
    best_profits = []
    nb_of_combinations = len(shares)

    for nb_of_shares in range(nb_of_combinations):
        best_shares_by_combination = get_best_shares_by_combination(shares, nb_of_shares+1)
        best_shares.append(best_shares_by_combination[0])
        best_profits.append(best_shares_by_combination[1])

    best_profit = max(best_profits)
    best_portfolio = ()
    for number_of_share in range(len(best_shares)):
        if best_profits[number_of_share] == best_profit:
            best_portfolio = best_shares[number_of_share]

    final_budget = 0
    for share in best_portfolio:
        share.price = round(share.price/100, 2)
        final_budget += share.price

    best_profit = round(best_profit/10000, 2)

    return final_budget, best_profit, best_portfolio
