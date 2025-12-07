# Supply Chain Analytics - Correlation Matrix Visualization

**Student Email:** 23f2004208@ds.study.iitm.ac.in

## Project Overview

This project analyzes supply chain performance data from 55 procurement transactions for an automotive manufacturer. The analysis identifies relationships between key supply chain metrics to optimize supplier selection, inventory planning, and cost management.

## Dataset Metrics

The analysis includes five critical supply chain variables:

1. **Supplier_Lead_Time**: Days from order placement to delivery
2. **Inventory_Levels**: Current stock quantities (units)
3. **Order_Frequency**: Number of orders placed per month
4. **Delivery_Performance**: On-time delivery rate (%)
5. **Cost_Per_Unit**: Unit cost in dollars ($)

## Key Findings

### Strong Correlations Identified:

- **Supplier Lead Time ↔ Cost Per Unit** (r = 0.97): Longer lead times strongly correlate with higher costs
- **Supplier Lead Time ↔ Delivery Performance** (r = -0.93): Longer lead times reduce on-time delivery
- **Order Frequency ↔ Cost Per Unit** (r = -0.90): More frequent orders reduce unit costs
- **Order Frequency ↔ Delivery Performance** (r = 0.85): Higher order frequency improves delivery rates

## Files Included

- `correlation.csv` - Full correlation matrix with all metric relationships
- `heatmap.png` - Excel-style visualization with Red-White-Green color scheme
- `supply_chain_analysis.py` - Python script for generating the analysis
- `q-excel-correlation-heatmap.xlsx` - Source data (55 transactions)

## Methodology

The correlation analysis was performed following Excel Data Analysis ToolPak best practices:
- Pearson correlation coefficients calculated for all variable pairs
- Conditional formatting applied using Red (negative) - White (neutral) - Green (positive) color scale
- Heatmap dimensions: 524×461 pixels (within required 400×400 to 512×512 range)

## Business Implications

**For OptimalFlow Logistics' Client:**

1. **Prioritize suppliers with shorter lead times** to reduce costs and improve delivery performance
2. **Increase order frequency** to leverage volume discounts and maintain better delivery schedules
3. **Monitor the lead time-cost relationship** as the strongest predictor of unit pricing
4. **Focus on delivery performance optimization** since it correlates strongly with multiple factors

---

*Analysis completed as part of Supply Chain Analytics coursework*  
*Repository: supplychainanalytics*  
*Owner: 23f2004208*
