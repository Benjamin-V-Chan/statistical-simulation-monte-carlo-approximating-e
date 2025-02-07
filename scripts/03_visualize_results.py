import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = "outputs/logs/simulation_log.csv"
VISUAL_OUTPUT_DIR = "outputs/visualizations"

def visualize_results():
    """Generates plots for convergence and distribution."""
    os.makedirs(VISUAL_OUTPUT_DIR, exist_ok=True)
    df = pd.read_csv(INPUT_FILE)

    # Convergence Plot
    plt.figure(figsize=(10, 5))
    plt.plot(df["Trial"], df["Cumulative_Avg"], label="Cumulative Average")
    plt.axhline(y=2.718, color="r", linestyle="--", label="True e")
    plt.xlabel("Trials")
    plt.ylabel("Estimated e")
    plt.title("Convergence of Estimated e")
    plt.legend()
    plt.savefig(f"{VISUAL_OUTPUT_DIR}/convergence_plot.png")
    plt.close()

    # Histogram
    plt.figure(figsize=(10, 5))
    plt.hist(df["Count"], bins=range(1, max(df["Count"]) + 1), density=True, alpha=0.7, edgecolor='black')
    plt.xlabel("Number of Random Draws Needed")
    plt.ylabel("Probability")
    plt.title("Distribution of Required Random Draws")
    plt.savefig(f"{VISUAL_OUTPUT_DIR}/histogram.png")
    plt.close()

if __name__ == "__main__":
    visualize_results()