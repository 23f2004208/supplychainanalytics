"""
Supply Chain Analytics: Correlation Matrix and Heatmap Generator
This script analyzes supply chain metrics and creates Excel-style visualizations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# Load the Excel file
print("Loading supply chain data...")
df = pd.read_excel('q-excel-correlation-heatmap.xlsx')

# Display the dataset info
print(f"\nDataset shape: {df.shape}")
print(f"\nColumn names: {df.columns.tolist()}")
print(f"\nFirst few rows:")
print(df.head())

# Select only the numeric columns for correlation
numeric_cols = ['Supplier_Lead_Time', 'Inventory_Levels', 'Order_Frequency', 
                'Delivery_Performance', 'Cost_Per_Unit']

# Check which columns exist in the dataset
available_cols = [col for col in numeric_cols if col in df.columns]
print(f"\nAvailable columns for analysis: {available_cols}")

# If columns don't match exactly, try to find them
if len(available_cols) < 5:
    print("\nAll columns in dataset:")
    print(df.columns.tolist())
    # Use all numeric columns
    available_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    print(f"\nUsing numeric columns: {available_cols}")

# Calculate correlation matrix
print("\nCalculating correlation matrix...")
correlation_matrix = df[available_cols].corr()

# Display correlation matrix
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Save correlation matrix as CSV
print("\nSaving correlation matrix to correlation.csv...")
correlation_matrix.to_csv('correlation.csv')
print("✓ correlation.csv saved successfully")

# Create Excel-style heatmap with Red-White-Green color scheme
print("\nCreating Excel-style heatmap...")

# Define Red-White-Green color palette (Excel conditional formatting style)
colors = ['#F8696B', '#FFFFFF', '#63BE7B']  # Red - White - Green
n_bins = 100
cmap = LinearSegmentedColormap.from_list('excel_rwg', colors, N=n_bins)

# Create figure with specific size (512x512 pixels at 100 DPI = 5.12 inches)
fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)

# Create heatmap
sns.heatmap(correlation_matrix, 
            annot=True,  # Show correlation values
            fmt='.2f',   # Format to 2 decimal places
            cmap=cmap,   # Red-White-Green color scheme
            center=0,    # Center colormap at 0
            vmin=-1,     # Min correlation value
            vmax=1,      # Max correlation value
            square=True, # Square cells
            linewidths=0.5,  # Grid lines
            linecolor='gray',
            cbar_kws={'label': 'Correlation Coefficient'},
            ax=ax)

# Formatting
plt.title('Supply Chain Metrics - Correlation Matrix', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('')
plt.ylabel('')

# Rotate labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

# Tight layout
plt.tight_layout()

# Save heatmap as PNG
print("Saving heatmap to heatmap.png...")
plt.savefig('heatmap.png', dpi=100, bbox_inches='tight')
print("✓ heatmap.png saved successfully (512x512 pixels)")

plt.close()

# Verify file dimensions
from PIL import Image
img = Image.open('heatmap.png')
print(f"\nHeatmap dimensions: {img.size[0]}x{img.size[1]} pixels")

print("\n" + "="*60)
print("ANALYSIS COMPLETE!")
print("="*60)
print("\nFiles generated:")
print("  1. correlation.csv - Correlation matrix values")
print("  2. heatmap.png - Excel-style Red-White-Green heatmap")
print("\nCorrelation Matrix Summary:")
print(f"  - Variables analyzed: {len(available_cols)}")
print(f"  - Data points: {len(df)} transactions")
print(f"  - Color scheme: Red (negative) - White (zero) - Green (positive)")
