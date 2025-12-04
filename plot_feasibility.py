import pandas as pd
import matplotlib.pyplot as plt

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
