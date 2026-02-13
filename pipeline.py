# =============================
# DATA PIPELINE PROJECT (ETL)
# =============================

import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# -----------------------------
# STEP 1: EXTRACT (Load Data)
# -----------------------------

print("Loading Raw Data...")

data = pd.read_csv("data/raw_data.csv")

print("\nRaw Data:")
print(data)

# -----------------------------
# STEP 2: TRANSFORM (Clean + Process)
# -----------------------------

print("\nCleaning Data...")

# Fill Missing Values
data["Salary"] = data["Salary"].fillna(data["Salary"].mean())

# Encode Department (Text → Number)
le = LabelEncoder()
data["Department"] = le.fit_transform(data["Department"])

# Scale Numerical Features
scaler = StandardScaler()
data[["Age", "Salary", "Experience"]] = scaler.fit_transform(
    data[["Age", "Salary", "Experience"]]
)

print("\nTransformed Data:")
print(data)

# -----------------------------
# STEP 3: LOAD (Save Processed Data)
# -----------------------------

print("\nSaving Processed Data...")

data.to_csv("data/processed_data.csv", index=False)

print("\nPipeline Completed Successfully!")