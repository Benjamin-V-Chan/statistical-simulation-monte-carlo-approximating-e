# statistical-simulation-monte-carlo-approximating-e

# Project Overview

This project simulates and analyzes a well-known Monte Carlo method for approximating Euler's number, $\( e \)$, using a statistical approach. The method works by generating random numbers between 0 and 1 and counting how many are needed for their sum to reach or exceed 1. The expected value of this count is approximately $\( e \)$.

---

# Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_simulation.py  # Runs the simulation and logs results
│   ├── 02_analyze_results.py      # Analyzes the logged results and computes estimates
│   ├── 03_visualize_results.py    # Generates visualizations of how e emerges
├── outputs/
│   ├── logs/                      # Stores raw simulation logs
│   ├── analysis/                  # Stores processed results and statistical analysis
│   ├── visualizations/            # Stores generated plots
├── requirements.txt               # Dependencies
├── README.md                      # Project documentation
```

---

# Usage

### 1. Setup the Project:

Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file:

```sh
pip install -r requirements.txt
```

### 2. Run the Simulation

This script runs the Monte Carlo simulation and logs results:

```sh
python scripts/01_generate_simulation.py
```

### 3. Analyze the Results

This script processes the raw simulation logs and computes statistical values:

```sh
python scripts/02_analyze_results.py
```

### 4. Visualize the Results

This script generates plots showing the convergence and distribution:

```sh
python scripts/03_visualize_results.py
```

---

# Requirements

- Python 3.x
- pandas
- matplotlib

Install dependencies using:

```sh
pip install -r requirements.txt
```