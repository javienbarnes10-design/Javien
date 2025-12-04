import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# --- NEW INTERACTIVE USER INPUT SECTION ---
print("\n--- Architectural Feasibility Data Entry ---")

options = []

while True:
    option_name = input("Enter Option Name (e.g., 'A', 'Scheme 1') or type 'done': ").strip()
    if option_name.lower() == 'done':
        break

    try:
        # User inputs are collected here
        area = float(input(f"Enter Area (SQFT) for {option_name}: "))
        cost = float(input(f"Enter Cost (Millions $) for {option_name}: "))
        coverage = float(input(f"Enter Zoning Coverage Percent for {option_name}: "))
        
        # Data is stored in the options list
        options.append({
            'Option': option_name,
            'Area_SQFT': area,
            'Cost_Millions': cost,
            'Coverage_Percent': coverage
        })
        print("Option added.\n")
    except ValueError:
        print("Invalid number input. Please try again.\n")

if not options:
    print("No data entered. Exiting script.")
    exit()

# 1. Load the data into a DataFrame
df = pd.DataFrame(options)
# ----------------------------------------


# 2. Calculate a key architectural metric (Cost Efficiency)
# This calculates the cost per square foot for each option.
df['Cost_per_SQFT'] = (df['Cost_Millions'] * 1_000_000) / df['Area_SQFT']

# --- REPORT ANALYSIS SECTION ---
# 2.5 Find the most efficient option (Lowest Cost per SQFT)
# idxmin() finds the index of the minimum value in the Cost_per_SQFT column
best_option_row = df.loc[df['Cost_per_SQFT'].idxmin()]

# Format the key values for the report
best_cost = f"${best_option_row['Cost_Millions']:.2f} Million"
best_sqft_cost = f"${best_option_row['Cost_per_SQFT']:,.0f}"

# -----------------------------------


# 3. Start plotting the data
# We plot Cost Efficiency (Y-axis) vs. Area (X-axis).
plt.figure(figsize=(10, 6))

# Use the 'Coverage_Percent' (Zoning constraint) to size the markers.
scatter = plt.scatter(
    df['Area_SQFT'],
    df['Cost_per_SQFT'],
    s=df['Coverage_Percent'] * 50, # Marker size scales with coverage constraint
    c=df['Cost_per_SQFT'],        # Marker color scales with cost
    cmap='viridis',               # Color map (shows gradient from low to high cost)
    alpha=0.7,
    edgecolors='w',
    linewidths=0.5
)

# 4. Add Labels and Title (Clear Communication)
plt.title('Architectural Feasibility Analysis: Cost Efficiency vs. Area')
plt.xlabel('Building Area (Square Feet)')
plt.ylabel('Cost Efficiency (Cost per SQFT)')

# Add annotations (labels) for each option
for i, row in df.iterrows():
    plt.annotate(
        row['Option'],
        (row['Area_SQFT'] + 500, row['Cost_per_SQFT']),
        fontsize=9
    )

# 5. Save the plot (Crucial step for Termux visualization)
plt.savefig('feasibility_plot.png')
print("\nPlot saved successfully as feasibility_plot.png")

# --- REPORT GENERATION SECTION ---
report_content = f"""
ARCHITECTURAL FEASIBILITY REPORT SUMMARY
----------------------------------------

Project Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Options Analyzed: {len(df)}

1. EFFICENCY FINDINGS
The analysis synthesized {len(df)} project options. The most efficient option based on raw construction cost per square foot is:

    OPTION NAME: {best_option_row['Option']}
    AREA: {best_option_row['Area_SQFT']:,.0f} SQFT
    TOTAL COST: {best_cost}
    COST PER SQFT: {best_sqft_cost}

2. ZONING NOTE
The efficient option ({best_option_row['Option']}) utilizes {best_option_row['Coverage_Percent']}% of the site coverage allowance.
*For a full visual assessment of all options and constraints, see feasibility_plot.png.*

"""

# Save the report to a plain text file
with open('feasibility_report.txt', 'w') as f:
    f.write(report_content)

print("Report saved successfully as feasibility_report.txt")
# -------------------------------------

