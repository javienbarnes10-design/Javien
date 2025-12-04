# Data-Driven Architectural Feasibility Analysis

## Project Overview
This project demonstrates a rigorous, command-line approach to early-stage architectural project assessment. It quickly synthesizes complex data—including **financial metrics, area requirements, and zoning constraints**—to provide a clear, visual feasibility report.

This tool ensures that design decisions are grounded in economic and regulatory viability before significant time is invested in schematic design.

## Architectural Felicity & Value
The core value of this tool is its **synthesis of constraints**. It utilizes systematic analysis (a core architectural skill) to solve the following problems:
* **Rapid Assessment:** Delivers key metrics (Cost per Square Foot) instantly.
* **Constraint Visualization:** Plots multiple variables simultaneously, allowing for immediate identification of the most efficient options that also meet zoning limits.

## Key Deliverables (Outputs)

1.  **Feasibility Plot (`feasibility_plot.png`):** A scatter plot visualizing the trade-off between **Cost Efficiency** (Y-axis) and **Total Area** (X-axis). The **marker size** is used to represent a critical third constraint (e.g., Zoning Coverage Percent).
2.  **Analyzed Data (`data.csv`):** The input table, including the derived `Cost_per_SQFT` metric.

## 🛠️ Usage (Running the Analysis)

This project requires Python 3, Pandas, and Matplotlib.

1.  **Input Data:** Edit the `data.csv` file to input your new project options, area estimates, and cost data.
2.  **Execute:** Run the primary script from the command line:
    ```bash
    python plot_feasibility.py
    ```
3.  **Output:** The script will automatically generate the `feasibility_plot.png` image in the current directory.
