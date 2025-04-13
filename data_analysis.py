import pandas as pd  # import numpy as np

# Sample dataset
data = {
    'A': [10, 20, 30, 40, 50],
    'B': [5, 15, 25, 35, 45],
    'C': [2, 8, 18, 32, 50]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute summary statistics
summary_stats = pd.DataFrame({
    'Mean': df.mean(),
    'Median': df.median(),
    'Standard Deviation': df.std()
})

# Display results
print(summary_stats)

