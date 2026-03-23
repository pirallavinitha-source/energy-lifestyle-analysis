import pandas as pd
import matplotlib.pyplot as plt

# ============================
# 📊 Your Data
# ============================
data = {
    "Date": [
        "1-Mar-26","2-Mar-26","3-Mar-26","4-Mar-26","5-Mar-26",
        "6-Mar-26","7-Mar-26","8-Mar-26","9-Mar-26","10-Mar-26",
        "11-Mar-26","12-Mar-26","13-Mar-26","14-Mar-26","15-Mar-26"
    ],
    "Energy Level": [4,3,5,2,4,3,5,2,4,3,5,2,4,3,5],
    "Sleep Hours": [7,6,8,5,7,6,8,5,7,6,8,5,7,6,8],
    "Water Intake (L)": [2.5,2,3,1.5,2.5,2,3,1.5,2.5,2,3,1.5,2.5,2,3],
    "Screen Time (hrs)": [3,4,2,6,3,5,2,6,3,4,2,6,3,5,2],
    "Exercise_Num": [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

# ============================
# 📅 Fix Date
# ============================
df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')

# ============================
# 📈 1. Energy vs Date
# ============================
plt.figure()
plt.plot(df['Date'], df['Energy Level'], marker='o')
plt.title("Energy vs Date")
plt.xlabel("Date")              # X-axis
plt.ylabel("Energy Level")      # Y-axis
plt.xticks(rotation=45)
plt.show()

# ============================
# 📊 2. Sleep vs Energy
# ============================
plt.figure()
plt.scatter(df['Sleep Hours'], df['Energy Level'])
plt.title("Sleep vs Energy")
plt.xlabel("Sleep Hours")       # X-axis
plt.ylabel("Energy Level")      # Y-axis
plt.show()

# ============================
# 📊 3. Water vs Energy
# ============================
plt.figure()
plt.scatter(df['Water Intake (L)'], df['Energy Level'])
plt.title("Water vs Energy")
plt.xlabel("Water Intake (L)")  # X-axis
plt.ylabel("Energy Level")      # Y-axis
plt.show()

# ============================
# 📊 4. Screen vs Energy
# ============================
plt.figure()
plt.scatter(df['Screen Time (hrs)'], df['Energy Level'])
plt.title("Screen vs Energy")
plt.xlabel("Screen Time (hrs)") # X-axis
plt.ylabel("Energy Level")      # Y-axis
plt.show()

# ============================
# 📊 5. Exercise vs Energy
# ============================
plt.figure()
plt.scatter(df['Exercise_Num'], df['Energy Level'])
plt.title("Exercise vs Energy")
plt.xlabel("Exercise (0=No, 1=Yes)")  # X-axis
plt.ylabel("Energy Level")            # Y-axis
plt.xlim(0,1)
plt.show()
