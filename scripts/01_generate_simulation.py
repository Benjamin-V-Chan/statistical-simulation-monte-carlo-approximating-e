import random
import os

OUTPUT_FILE = "outputs/logs/simulation_log.csv"
NUM_TRIALS = 100000  # Adjust for desired accuracy

def single_trial():
    """Performs one trial of the e approximation method."""
    total = 0
    count = 0
    while total < 1:
        total += random.random()
        count += 1
    return count

def run_simulation():
    """Runs multiple trials and logs results."""
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    with open(OUTPUT_FILE, "w") as f:
        f.write("Trial,Count,Cumulative_Avg\n")
        cumulative_sum = 0

        for i in range(1, NUM_TRIALS + 1):
            count = single_trial()
            cumulative_sum += count
            avg_so_far = cumulative_sum / i
            f.write(f"{i},{count},{avg_so_far}\n")

if __name__ == "__main__":
    run_simulation()