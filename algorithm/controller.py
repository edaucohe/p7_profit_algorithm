from itertools import combinations
from typing import Optional, List

from algorithm.model import BUDGET_MAX, COMBINAISONS_NUMBER_MAX
from algorithm.view import View


class Controller:
    def __init__(self, shares: Optional[List] = None, view: Optional[View] = None):
        self.shares = shares or []
        self.view = view or View()

    def best_investment(self):
        all_combinations = []
        for combination in combinations(self.shares, COMBINAISONS_NUMBER_MAX):
            all_combinations.append(combination)
        self.view.console_display(len(all_combinations))

        combinations_below_budget_max = []
        for every_combination in all_combinations:
            price_sum = 0
            for share in every_combination:
                price_sum = share.get_investment_sum(price_sum)
            if price_sum <= BUDGET_MAX:
                combinations_below_budget_max.append(every_combination)
        self.view.console_display(len(combinations_below_budget_max))

        profits_by_combination = []
        for combination in combinations_below_budget_max:
            profits = 0
            for share in combination:
                profit = share.get_profit()
                profits += profit
            profits_by_combination.append(profits)
        self.view.console_display(profits_by_combination)

        best_investment = ()
        best_profit = max(profits_by_combination)
        self.view.console_display(best_profit)
        for combination_number in range(len(combinations_below_budget_max)):
            if profits_by_combination[combination_number] == best_profit:
                best_investment = combinations_below_budget_max[combination_number]

        self.view.console_display(best_investment)

    def run(self, shares):
        self.shares = shares
        self.best_investment()
