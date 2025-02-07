import pandas as pd
import os

INPUT_FILE = "outputs/logs/simulation_log.csv"
OUTPUT_FILE = "outputs/analysis/simulation_analysis.txt"

def analyze_results():
    """Reads simulation log and computes statistics."""
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    
    df = pd.read_csv(INPUT_FILE)
    estimated_e = df["Cumulative_Avg"].iloc[-1]
    std_dev = df["Count"].std()
    
    with open(OUTPUT_FILE, "w") as f:
        f.write(f"Estimated e: {estimated_e}\n")
        f.write(f"Standard Deviation: {std_dev}\n")
        f.write(f"Total Trials: {len(df)}\n")

if __name__ == "__main__":
    analyze_results()