from dataclasses import dataclass
from typing import Dict

BUDGET_MAX = 500
CSV_FILES_NAME = ['resources/dataset1_Python+P7.csv', 'resources/dataset2_Python+P7.csv']


@dataclass
class Share:
    name: str
    price: float
    profit: float

    def get_investment_sum(self, price_sum):
        price_sum += self.price
        return price_sum

    def get_profit(self):
        return self.price*self.profit

    @staticmethod
    def deserialize_csv_file(row_from_csv_file: Dict) -> 'Share':
        return Share(**row_from_csv_file)
