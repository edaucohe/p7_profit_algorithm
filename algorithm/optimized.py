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
    return get_best_shares_by_knapsack_algorithm(shares)

    # partial_budget = BUDGET_MAX * 100
    # nb_of_share = len(shares)
    # best_portfolio = []
    #
    # while partial_budget >= 0 and nb_of_share >= 0:
    #     current_share = shares[nb_of_share-1]
    #     if matrix_of_profits[nb_of_share][partial_budget] == \
    #             matrix_of_profits[nb_of_share-1][partial_budget-current_share.price]+current_share.profit:
    #         best_portfolio.append(current_share)
    #         partial_budget -= current_share.price
    #     nb_of_share -= 1
    #
    # return best_portfolio

    # best_shares = []
    # best_profits = []
    # nb_of_combinations = len(shares)
    # # nb_of_combinations = 1
    # for nb_of_shares in range(nb_of_combinations):
    #     best_shares_by_combination = get_best_shares_by_knapsack_problem(shares)
    #     best_shares.append(best_shares_by_combination[0])
    #     best_profits.append(best_shares_by_combination[1])
    #
    # best_profit = max(best_profits)
    # best_portfolio = ()
    # for number_of_share in range(len(best_shares)):
    #     if best_profits[number_of_share] == best_profit:
    #         best_portfolio = best_shares[number_of_share]
    #
    # print("\nLe meilleur bénéfice", best_profit)
    # print("Le meilleur investissement", best_portfolio)


# def main():
#     shares = create_share_db()
#     get_best_shares_by_knapsack_problem(shares)
#
#
# if __name__ == "__main__":
#     main()
