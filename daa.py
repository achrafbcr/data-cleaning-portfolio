import pandas as pd
import numpy as np
from sympy import false


# Create messy employee data
data = {
    'EmployeeID': [101, 102, 102, 103, 104, 105, 106, np.nan, 108, 109],
    'Name': ['Ahmed Khan ', ' Fatima Zahra', 'fatima zahra', 'Mohammed Ali', 'Aisha Hassan', 'omar farouk', 'Sara Ahmed', 'Khalid ', 'Nadia Salem', 'Youssef'],
    'Age': [25, 34, 34, 45, 29, 'thirty', 38, 52, np.nan, 41],
    'Salary': [45000, 62000, 62000, 89000, 52000, 67000, 999999, 71000, 48000, 55000],
    'Department': ['IT', 'HR', 'hr', 'Finance', 'Marketing', 'IT', 'Operations', 'Finance', 'HR', 'it'],
    'Join_Date': ['2023-01-15', '2022-06-30', '2022-06-30', '2021-03-12', '2024-01-01', '2023-11-20', '2020-09-05', '2022-02-28', '2023-07-10', '2021-12-01']
}
df = pd.DataFrame(data)
df.to_csv('messy_employee.csv')
print("✅ Dataset created successfully!")
print(df)


print(df.head(10))
print(df.shape)
print("=="*50)
print(df.info())
print("=="*50)
print(df.describe())
print("=="*50)
print(df.isnull().sum())
print("=="*50)
print(df.duplicated().sum())
print("=="*50)
print(df['Department'].value_counts())

print("Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nAge describe:\n", df['Age'].describe())
print("\nSalary describe:\n", df['Salary'].describe())
print("\nDepartment value counts:\n", df['Department'].value_counts())
print("\nJoin_Date type:", df['Join_Date'].dtype)


# Make a safe copy
df_clean = df.copy()

# 1. Clean Name: remove extra spaces, make proper capital letters
df_clean['Name'] = df_clean['Name'].str.strip().str.title()

# 2. Clean Department: remove spaces, make all lowercase first, then title
df_clean['Department'] = df_clean['Department'].str.strip().str.lower().str.title()

print("After string cleaning:")
print(df_clean[['Name', 'Department']].to_string())
print("\nDuplicates after cleaning:", df_clean.duplicated().sum())

print(df_clean[df_clean.duplicated()])

df_clean=df_clean.drop_duplicates()
df_clean['Age']=df_clean['Age'].replace('thirty',30)
df_clean['Age']=pd.to_numeric(df_clean['Age'], errors='coerce')

print("After removing duplicate and fixing Age:")
print(df_clean)
print("\nMissing values now:\n", df_clean.isnull().sum())
print("\nData types now:\n", df_clean.dtypes)

# === FINAL CLEANING BLOCK ===
df_clean = df_clean.copy()   # safety copy

# 1. Fix missing EmployeeID (assign next ID)
df_clean['EmployeeID'] = df_clean['EmployeeID'].fillna(110)

# 2. Fix missing Age (fill with median)
df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())

# 3. Fix crazy Salary outlier
median_salary = df_clean[df_clean['Salary'] < 200000]['Salary'].median()
df_clean['Salary'] = df_clean['Salary'].replace(999999, int(median_salary))

# 4. Make EmployeeID integer + Join_Date real date
df_clean['EmployeeID'] = df_clean['EmployeeID'].astype(int)
df_clean['Join_Date'] = pd.to_datetime(df_clean['Join_Date'])

# Show the final result
print("✅ FULLY CLEANED DATASET:")
print(df_clean.to_string(index=False))
print("\nMissing values (should be 0):")
print(df_clean.isnull().sum())
print("\nFinal data types:")
print(df_clean.dtypes)
print("\nSummary stats:")
print(df_clean.describe())




df_clean.to_csv('clean_employee.csv', index=false)










"""
print("=="*50)

df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')
df['year']=df['JoinDate'].df.year

print("===="*50)
# === EXPLORATION - Let's understand our messy data ===
#print("="*50)
#print(df)

#print("=== Shape of the dataset ===")
#print(df.shape)

#print("\n=== Data types and missing values ===")
#print(df.info())

#print("\n=== Basic statistics (numerical columns) ===")
#print(df.describe())

#print("\n=== Number of missing values per column ===")
#print(df.isnull().sum())

#print("\n=== Number of duplicate rows ===")
#print(df.duplicated().sum())

#print("\n=== Unique values in Department ===")
#print(df['Department'].value_counts())

#print("\n=== Unique values in Name (showing duplicates) ===")
#print(df['Name'].value_counts())


# === START CLEANING ===
#print(df)
#print("="*50)
df_clean = df.copy()  # Always work on a copy!

# 1. Fix data types & handle missing EmployeeID (drop the row with None)
df_clean = df_clean.dropna(subset=['EmployeeID'])  # Drops the row with missing ID
df_clean['EmployeeID'] = df_clean['EmployeeID'].astype(int)

df_clean= df_clean.drop_duplicates(subset=['EmployeeID'] , keep='first')
print(f"✅ Removed {len(df) - len(df_clean)} problematic rows (missing ID + outlier + duplicates)")
median_age = df_clean['Age'].median()
median_salary = df_clean['Salary'].median()
df_clean['Age'] = df_clean['Age'].fillna(median_age)
df_clean['Salary'] = df_clean['Salary'].fillna(median_salary)

# 3. Fix outliers in Age (remove crazy 999)
df_clean = df_clean[df_clean['Age'] < 100]  # Simple rule for now: age < 100

# 4. Clean strings: lowercase, strip spaces, fix department casing
df_clean['Name'] = df_clean['Name'].str.strip().str.lower().str.title()  # " sara ahmed " → "Sara Ahmed"
df_clean['Department'] = df_clean['Department'].str.strip().str.upper()  # "hr " → "HR", "Finance " → "FINANCE"

# 5. Fix JoinDate (make it real datetime, handle incomplete one)
df_clean['JoinDate'] = pd.to_datetime(df_clean['JoinDate'], errors='coerce')  # Bad dates become NaT

#print("✅ Cleaning done!")
#print("\nCleaned dataset (first 5 rows):")
#print(df_clean.head())

#print("\nNew missing values:")
#print(df_clean.isnull().sum())

#print("\nNew shape:")
#print(df_clean.shape)
#print("="*50)
#print(df_clean.describe())
print("="*50)
print(df_clean)

# ====================== AFFICHAGE DES LIGNES SUPPRIMÉES ======================
print("\n" + "="*80)
print("📋 LIGNES QUI ONT ÉTÉ SUPPRIMÉES pendant le nettoyage")
print("="*80)

# On compare l'original et le cleané grâce à EmployeeID (c'est le plus fiable)
lignes_supprimees = df[~df['EmployeeID'].isin(df_clean['EmployeeID'])]

print(f"\n✅ Total de lignes supprimées : {len(lignes_supprimees)} / {len(df)}")
print(lignes_supprimees)

# Affichage détaillé par raison (très utile pour comprendre)
print("\n" + "-"*60)
print("DÉTAIL PAR RAISON :")

# 1. Ligne sans EmployeeID
print("\n1. Ligne(s) supprimée(s) car EmployeeID manquant :")
print(df[df['EmployeeID'].isnull()])

# 2. Outlier Age
print("\n2. Ligne(s) supprimée(s) car Age >= 100 (outlier) :")
print(df[df['Age'] >= 100])

# 3. Doublons EmployeeID
print("\n3. Ligne(s) supprimée(s) car doublon EmployeeID :")
# On regarde les doublons dans les données originales (après nettoyage des noms)
temp = df.dropna(subset=['EmployeeID']).copy()
temp['Name_clean'] = temp['Name'].str.strip().str.lower().str.title()
doublons = temp[temp.duplicated(subset=['EmployeeID'], keep=False)]
print(doublons.sort_values('EmployeeID'))

"""