from dataclasses import dataclass


BUDGET_MAX = 500


@dataclass
class Share:
    name: str
    price: int
    profit_percentage: float

    def get_investment_sum(self, price_sum):
        price_sum += self.price
        return price_sum

    def get_profit(self):
        return self.price*self.profit_percentage
