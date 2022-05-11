from dataclasses import dataclass
from typing import Dict
# from enum import Enum

# from algorithm import bruteforce, optimized

BUDGET_MAX = 500
CSV_FILES_NAME = ['resources/dataset1_Python+P7.csv', 'resources/dataset2_Python+P7.csv']
CSV_FILE_0 = ['resources/dataset0_bruteforce+P7.csv']
CSV_FILE_1 = ['resources/dataset1_Python+P7.csv']
CSV_FILE_2 = ['resources/dataset2_Python+P7.csv']


@dataclass
class Share:
    name: str
    price: int
    profit: float

    def get_investment_sum(self, price_sum):
        price_sum += self.price
        return price_sum

    def get_profit(self):
        return self.price*self.profit

    @staticmethod
    def deserialize_from_csv_file(row_from_csv_file: Dict[str, any]) -> 'Share':
        row_from_csv_file['price'] = int(float(row_from_csv_file['price'])*100)
        row_from_csv_file['profit'] = float(row_from_csv_file['profit'])
        return Share(**row_from_csv_file)


# class Portfolio (Enum):
#     BRUTEFORCE_FUNC: bruteforce
#     OPTIMIZED_FUNC: optimized
