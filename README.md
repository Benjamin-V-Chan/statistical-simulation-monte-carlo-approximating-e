# statistical-simulation-monte-carlo-approximating-e

# Project Overview

This project simulates and analyzes a well-known Monte Carlo method for approximating Euler's number, $\( e \)$, using a statistical approach. The method works by generating random numbers between 0 and 1 and counting how many are needed for their sum to reach or exceed 1. The expected value of this count is approximately $\( e \)$.

## Mathematical Proof of the Approximation

Euler's number, $\( e \)$, can be defined as:

$$e = \sum_{k=0}^{\infty} \frac{1}{k!}$$

### Step-by-Step Derivation

Define a random variable $\( \xi \)$ as the minimum number of uniform random variables $\( r_i \sim U(0,1) \)$ required such that their sum exceeds 1:

$$\xi = \min \left\{ n \mid \sum_{i=1}^{n} r_i > 1 \right\}$$

We seek to determine $\( E[\xi] \)$, the expected value of $\( \xi \)$, and prove that $\( E[\xi] = e \)$.

### Probability Mass Function (PMF) of $\( \xi \)$

The probability that exactly $\( k \)$ samples are needed to exceed 1 is given by:

$$P(\xi = k) = P \left( \sum_{i=1}^{k-1} r_i \leq 1, \sum_{i=1}^{k} r_i > 1 \right)$$

Since the sum of $\( k-1 \)$ uniform variables follows a gamma distribution with shape $\( k-1 \)$ and scale 1, we obtain:

$$P(\xi = k) = \int_0^1 \frac{x^{k-1}}{(k-1)!} dx = \frac{1}{k!}$$

### Expected Value of $\( \xi \)$

By definition, the expectation is:

$$E[\xi] = \sum_{k=1}^{\infty} k P(\xi = k)$$

Substituting $\( P(\xi = k) = \frac{1}{k!} \)$:

$$E[\xi] = \sum_{k=1}^{\infty} k \frac{1}{k!}$$

Using summation by parts, we rewrite:

$$\sum_{k=1}^{\infty} k \frac{1}{k!} = \sum_{k=1}^{\infty} \left( \frac{k}{k!} \right)$$

Observing that $\( k/k! = 1/(k-1)! \)$, we shift the index:

$$E[\xi] = \sum_{m=0}^{\infty} \frac{1}{m!} = e$$

### Conclusion

Thus, the expected value of $\( \xi \)$ is precisely $\( e \)$, meaning that our Monte Carlo simulation naturally converges to $\( e \)$ as the number of trials increases.

### Citation

The concept of estimating $\( e \)$ using simulation is derived from:

Russell, K. G. "Estimating the Value of e by Simulation." *The American Statistician*, vol. 45, no. 1, 1991, pp. 66–68. JSTOR, [https://doi.org/10.2307/2685243](https://doi.org/10.2307/2685243). Accessed 7 Feb. 2025.

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
