import pandas as pd

# ÚLOHA 1
df = pd.read_csv("dataset.csv")
print(df.head())
print(df.info())
print("Počet řádků:", df.shape[0])
print("Počet sloupců:", df.shape[1])

# ÚLOHA 2
cols_numeric = ["voltage_v", "current_a", "power_w", "angle_deg", "light_intensity_lux"]

for col in cols_numeric:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

df = df[df["angle_deg"] <= 90]
df = df[df["angle_deg"] >= 0]
df = df[df["power_w"] >= 0]
df = df[df["light_intensity_lux"] >= 0]

df = df.dropna()
df = df.drop_duplicates()

df["weather"] = df["weather"].str.strip().str.lower()
df["room"] = df["room"].str.strip().str.lower()

df["weather"] = df["weather"].replace({"suny": "sunny"})

# ÚLOHA 3
df["power_calc"] = df["voltage_v"] * df["current_a"]
diff = df["power_calc"] - df["power_w"]
print(diff.describe())

# ÚLOHA 4
angle_analysis = df.groupby("angle_deg")["power_w"].mean()
print(angle_analysis)

# ÚLOHA 5
correlation = df["light_intensity_lux"].corr(df["power_w"])
print("Korelace:", correlation)

# ÚLOHA 6
environment = df.groupby("room")["power_w"].mean()
print(environment)

# ÚLOHA 7
best = df.loc[df["power_w"].idxmax()]
print(best)

# ÚLOHA 8
print(df.nlargest(5, "power_w"))
print(df.nlargest(5, "light_intensity_lux"))

# ÚLOHA 9
high_lux = df[df["light_intensity_lux"] > 500]
analysis = high_lux.groupby("angle_deg")["power_w"].mean()
print(analysis)
