from typing import List

from algorithm.controller import Controller
from algorithm.model import Share


def create_share_db() -> List:
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


def main():
    shares = create_share_db()
    controller = Controller()
    controller.run(shares)

from algorithms import bruteforce, optimized_v1
    
ALGORITHM_PROVIDER: Dict[str, Callable[[List[Share], Portfolio]] = {
   'bruteforce': bruteforce.get_best_portfolio,
}

def main2(shares_filepath: str = 'resources/shares-short.csv', algorithm: str = 'bruteforce'):
    shares = load_shares(shares_filepath)
    algorithm_func: Callable[[List[Share], Portfolio] = ALGORITHM_PROVIDER[algorithm]
    
    best_portfolio = algorithm_func(shares)
    
    nice_print(best_portfolio)
    

if __name__ == "__main__":
    main()
