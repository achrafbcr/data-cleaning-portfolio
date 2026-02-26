# Data Cleaning Portfolio - Achraf

**My first professional data cleaning project using Python & Pandas**

### Project Goal
Transform a messy, real-world employee dataset into clean, ready-to-use data that a company can trust for reports, payroll, or analysis.

### 📊 Before vs After

| File                  | Status          | Issues Fixed                          |
|-----------------------|-----------------|---------------------------------------|
| `messy_employee.csv`  | Raw & Dirty     | 10 rows with problems                 |
| `clean_employee.csv`  | Clean & Ready   | 100% fixed, professional quality      |

### ✅ What I Fixed
- Removed duplicate records (Fatima Zahra appeared twice)
- Handled missing values (EmployeeID & Age)
- Fixed inconsistent text (names, departments, extra spaces)
- Corrected wrong data types (Age as text → number, Join_Date as text → real date)
- Detected and fixed outlier (salary = 999999 → realistic value)
- Standardized everything (proper capitalization, no extra spaces)

### 🛠️ Tools & Skills Used
- **Python** (pandas, numpy)
- Data exploration (`head`, `info`, `describe`, `isnull`, `duplicated`)
- String cleaning (`.str.strip()`, `.str.title()`, `.str.lower()`)
- Handling missing values (`fillna`, `drop_duplicates`)
- Outlier detection & fixing (median method)
- Data type conversion (`pd.to_numeric`, `pd.to_datetime`)
- Saving clean output (`to_csv`)

### How to Run the Project
```bash
pip install pandas numpy
python daa.py
