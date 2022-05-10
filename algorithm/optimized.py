from typing import List

from algorithm.model import Share, BUDGET_MAX


def get_best_shares_by_knapsack_algorithm(shares: List[Share]):
    matrix_of_profits = [[0 for column in range(BUDGET_MAX*100+1)] for row in range(len(shares)+1)]

    for nb_of_share in range(1, len(shares)+1):
        current_share = shares[nb_of_share-1]
        current_share_profit = current_share.get_profit()
        for partial_budget in range(1, BUDGET_MAX*100+1):
            if current_share.price <= partial_budget:
                matrix_of_profits[nb_of_share][partial_budget] = max(
                    matrix_of_profits[nb_of_share-1][partial_budget],
                    current_share_profit + matrix_of_profits[nb_of_share-1][partial_budget-current_share.price]
                )
            else:
                matrix_of_profits[nb_of_share][partial_budget] = matrix_of_profits[nb_of_share - 1][partial_budget]

    return matrix_of_profits


def get_best_portfolio(shares: List[Share]):
    matrix_of_profits = get_best_shares_by_knapsack_algorithm(shares)

    nb_of_shares = len(shares)
    partial_budget = BUDGET_MAX*100
    best_portfolio = []

    while partial_budget >= 0 and nb_of_shares >= 0:
        current_share = shares[nb_of_shares-1]
        if matrix_of_profits[nb_of_shares][partial_budget] == \
                matrix_of_profits[nb_of_shares-1][partial_budget-current_share.price]+current_share.get_profit():
            best_portfolio.append(current_share)
            partial_budget -= current_share.price
        nb_of_shares -= 1

    return matrix_of_profits[-1][-1], best_portfolio
