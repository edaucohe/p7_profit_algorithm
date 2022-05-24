import csv
import time
from typing import List
import numpy as np
from matplotlib import pyplot as plt

from algorithm import bruteforce, optimized
from algorithm.model import *


ACTIONS_NB = 20


def pick_n_shares(shares, actions_counts):
    if len(shares) >= actions_counts:
        for actions_count in range(len(shares)-actions_counts):
            shares.pop(-1)
    else:
        print("La valeur doit être plus petite que le nombre d'actions ")
    return shares


def load_shares(files_name: List[str]) -> List[Share]:
    shares = []
    for file_name in files_name:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                share_cts = Share.deserialize_from_csv_file(row)
                if share_cts.price > 0:
                    shares.append(share_cts)
    return shares


def plot_ram_usage(bruteforce_peak_ram, optimized_peak_ram, nb_of_shares):
    x_axis = np.array(range(1, nb_of_shares+1))
    y1_axis = np.array(bruteforce_peak_ram)
    y2_axis = np.array(optimized_peak_ram)

    plt.plot(x_axis, y1_axis, label="bruteforce algorithm peak RAM")
    plt.plot(x_axis, y2_axis, label="optimized algorithm peak RAM")
    plt.title("Plot of peak RAM")
    plt.xlabel("Number of actions")
    plt.ylabel("Peak RAM (MB)")

    plt.legend()
    plt.show()


def plot_execution_time(bruteforce_execution_time, optimized_execution_time, nb_of_shares):
    x_axis = np.array(range(1, nb_of_shares+1))
    y1_axis = np.array(bruteforce_execution_time)
    y2_axis = np.array(optimized_execution_time)
    plt.plot(x_axis, y1_axis, label="bruteforce algorithm execution_time")
    plt.plot(x_axis, y2_axis, label="optimized algorithm execution_time")

    plt.title("Plot of Execution time")
    plt.xlabel("Number of actions")
    plt.ylabel("Execution time (s)")

    plt.legend()
    plt.show()


def measure_algorithm(algorithm_func, shares):
    algorithm_delay_start = time.time()
    final_budget, best_investment, best_portfolio, peak_ram = algorithm_func(shares)
    algorithm_delay_end = time.time()
    execution_time = algorithm_delay_end - algorithm_delay_start

    print(f"\nTemps d'exécution : "
          f"{round(execution_time, 2)} secondes")

    return {
        "execution_time": execution_time,
        "peak_ram": peak_ram,
        "best_portfolio": best_portfolio
    }


def plot_performance(shares_filepath: List[str], actions_nb: int):
    bruteforce_peaks_ram = []
    optimized_peaks_ram = []
    bruteforce_execution_time = []
    optimized_execution_time = []
    for action_nb in range(actions_nb):
        # Get bruteforce performance info
        shares: List[Share] = load_shares(shares_filepath)
        new_shares = pick_n_shares(shares, action_nb+1)
        bruteforce_data = measure_algorithm(bruteforce.get_best_portfolio, new_shares)
        bruteforce_peaks_ram.extend(bruteforce_data['peak_ram'])
        bruteforce_execution_time.append(bruteforce_data['execution_time'])

        # Get optimized performance info
        shares: List[Share] = load_shares(shares_filepath)
        new_shares = pick_n_shares(shares, action_nb+1)
        optimized_data = measure_algorithm(optimized.get_best_portfolio, new_shares)
        optimized_peaks_ram.extend(optimized_data['peak_ram'])
        optimized_execution_time.append(optimized_data['execution_time'])

    # Plot performances info
    plot_ram_usage(bruteforce_peaks_ram, optimized_peaks_ram, actions_nb)
    plot_execution_time(bruteforce_execution_time, optimized_execution_time, actions_nb)


plot_performance(CSV_FILE_0, ACTIONS_NB)
