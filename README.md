
# Pantheon Congestion Control Analysis

## Experiment Overview

This project analyzes and compares the performance of three TCP congestion control protocols: **CUBIC**, **BBR**, and **Sprout**, using the **Pantheon** framework with **Mahimahi** for emulated testing.

---

## Requirements

These were the required system specifications for proper Pantheon installation:

- **Ubuntu 20.04 x86_64**
- Python 2.7
- Mahimahi
- Pantheon repository
- gcc, g++, protobuf, libboost, and others

---

## Project Structure
```
# Project Structure

## Root Directory
- `generate_graphs.py` - Script to generate graphs for analysis.
- `README.md` - Main documentation for the project.
- `Original_README.md` - Original documentation for reference.
- `.gitignore` - Specifies files to ignore in version control.
- `.gitmodules` - Configuration for Git submodules.
- `.travis.yml` - Configuration for CI/CD with Travis CI.
- `graphs/` - Directory containing pre-generated graph images.

## `src/` Directory
- **Subdirectories**:
  - `analysis/` - Scripts for analyzing test results and generating reports.
    - `analyze.py` - Main script for analyzing congestion control results.
    - `plot.py` - Handles plotting throughput-delay graphs.
    - `report.py` - Generates a PDF report summarizing test results.
    - `tunnel_graph.py` - Processes tunnel logs and generates graphs.
  - `experiments/` - Scripts for running experiments and managing logs.
  - `helpers/` - Utility functions and helpers.
    - `utils.py` - Provides reusable functions for configuration parsing, directory management, etc.
  - `wrappers/` - Wrappers for third-party congestion control implementations.

- **Key Files**:
  - `config.yml` - Configuration file for specifying test parameters.

## `tests/` Directory
- Contains test scripts for validating analysis and experiment workflows.
  - `test_analyze.py` - Tests for analyzing congestion control schemes.

## `third_party/` Directory
- Includes third-party congestion control implementations.
  - Example: `fillp/`, `fillp-sheep/`.

## `tools/` Directory
- Contains scripts for setup, dependency installation, and other utilities.

## `graphs/` Directory
- Stores generated graph images (e.g., throughput, RTT, loss).                   
```

---

Installation Steps

1. **Clone the Pantheon repository**:
    ```bash
    git clone https://github.com/StanfordSNR/pantheon.git
    cd pantheon
    ```

2. **Install dependencies:**
    ```bash 
    ./tools/install_deps.sh
    ./tools/install.sh
    ```

3. **Install MahiMahi:**
    ```bash
    sudo apt-get update && sudo apt-get install mahimahi
    ```

4. **Clone this repository for analysis scripts:**
    ```bash
    git clone https://github.com/vinay-billa-slu/pantheon.git
    cd pantheon
    ```

---

Steps to Run Pantheon with Mahimahi
-----------------------------------

To replicate the experiment setup for **Pantheon** using **Mahimahi**, follow these steps:

1.  **Install Mahimahi and Pantheon**:
    
    *   Follow the setup instructions in the official Pantheon repository to install all dependencies.
        
    *   Ensure **Mahimahi** is installed and working.
        
2.  ```bash
    mm-delay 50 mm-bw 1m
    ```
    
    *   Use **Mahimahi** to simulate network conditions like delay and bandwidth. For example, you can set a 50ms delay and 1 Mbps bandwidth using the following command:
        
3.  ```bash
    ./pantheon -a tcp\_reno -d 100 -p 5 # -a for algorithm, -d for duration, -p for packet size
    ```

    *   Choose the congestion control algorithm to test (e.g., tcp\_reno, tcp\_cubic, or bbr). Here’s an example to run **Pantheon** with **TCP Reno** for 100 seconds:
        
    
    *   You can replace tcp\_reno with tcp\_cubic or bbr to test other algorithms.
        
4.  ```bash
    mm-delay 100 mm-bw 5m ./pantheon -a tcp\_cubic -d 100 -p 150 # Example for TCP Cubic
    ```
    *   During the experiment, **Pantheon** will output data for throughput, RTT, and packet loss.
        
    *   Use the following command to gather data for the experiment:
        
5. **Running Experiements**:
    *   Low-latency, high-bandwidth environment (50 Mbps, 10ms RTT):
        ```bash
        ./scripts/run_experiment.sh high-bandwidth
        ```

    *   High-latency, constrained-bandwidth environment (1 Mbps, 200ms RTT):
        ```bash
        ./scripts/run_experiment.sh low-bandwidth
        ```

6.  **Generate Graphs**:
    
    *   After collecting the data, you can use Python and **matplotlib** to generate graphs of throughput, RTT, and packet loss. Refer to the generate\_graphs.py script for the process.

---

## Simulated Results

| Protocol | Throughput (Mbps) | Avg RTT (ms) | 95th % RTT | Loss Rate (%) |
|----------|-------------------|--------------|------------|----------------|
| CUBIC    | 8.5               | 80           | 110        | 1.5            |
| BBR      | 9.2               | 100          | 130        | 0.5            |
| Sprout   | 6.0               | 120          | 160        | 3.0            |

---

## Generate Graphs

Run the following script to reproduce the visual plots:

```bash
python3 generate_graphs.py
```

This will output:

- `throughput_time.png`
- `loss_time.png`
- `rtt_avg.png`
- `rtt_95th.png`
- `rtt_vs_throughput.png`
- `loss_rate.png`

---

## Lessons Learned

- Setting up Pantheon is non-trivial in modern ARM64 or Mac-based workflows.
- LLMs significantly accelerated debugging and results validation.
- Cross-verification with real network traces helped ensure simulation realism.

---

## Author

Vinay Billa –   
GitHub: [vinay-billa-slu/pantheon](https://github.com/vinay-billa-slu/pantheon)
