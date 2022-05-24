from memory_profiler import memory_usage
from typing import List

from algorithm.model import Share, BUDGET_MAX_CTS


def get_best_shares_by_knapsack_algorithm(shares: List[Share]):
    matrix_of_profits = [[0 for column in range(BUDGET_MAX_CTS + 1)] for row in range(len(shares) + 1)]

    for nb_of_share in range(1, len(shares)+1):
        current_share = shares[nb_of_share-1]
        current_share_profit = current_share.get_profit()
        for partial_budget_cts in range(1, BUDGET_MAX_CTS + 1):
            if current_share.price <= partial_budget_cts:
                matrix_of_profits[nb_of_share][partial_budget_cts] = max(
                    # Last best profit
                    matrix_of_profits[nb_of_share-1][partial_budget_cts],
                    # Current profit
                    current_share_profit + matrix_of_profits[nb_of_share-1][partial_budget_cts-current_share.price]
                )
            else:
                matrix_of_profits[nb_of_share][partial_budget_cts] = \
                    matrix_of_profits[nb_of_share - 1][partial_budget_cts]

    return matrix_of_profits


def get_best_portfolio(shares: List[Share]):
    matrix_of_profits = get_best_shares_by_knapsack_algorithm(shares)

    nb_of_shares = len(shares)
    partial_budget_cts = BUDGET_MAX_CTS
    best_portfolio = []

    while partial_budget_cts >= 0 and nb_of_shares >= 0:
        current_share = shares[nb_of_shares-1]
        if matrix_of_profits[nb_of_shares][partial_budget_cts] == \
                matrix_of_profits[nb_of_shares-1][partial_budget_cts-current_share.price]+current_share.get_profit():
            best_portfolio.append(current_share)
            partial_budget_cts -= current_share.price
        nb_of_shares -= 1

    final_budget = 0
    for share in best_portfolio:
        share.price = round(share.price/100, 2)
        final_budget += share.price

    best_profit = round(matrix_of_profits[-1][-1]/10000, 2)
    ram_memory = memory_usage()

    return final_budget, best_profit, best_portfolio, ram_memory
