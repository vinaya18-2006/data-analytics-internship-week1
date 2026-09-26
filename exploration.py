import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Load dataset
df = pd.read_csv('telco-churn.csv')

# Structural metadata
print("=== DATASET OVERVIEW ===")
print(f"Total Rows (Observations): {df.shape[0]}")
print(f"Total Columns (Features):  {df.shape[1]}")
print("\n=== COLUMN DATA TYPES ===")
print(df.dtypes)
print("\n=== FIRST 5 OBSERVATIONS ===")
df.head()
