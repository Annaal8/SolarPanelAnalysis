import polars as pl

# ÚLOHA 1
df = pl.read_csv("dataset.csv")
print(df.head())
print("Shape:", df.shape)
print("Schema:", df.schema)

# ÚLOHA 2
df = df.with_columns([
    pl.col("voltage_v").cast(pl.Float64),
    pl.col("current_a").cast(pl.Float64),
    pl.col("power_w").cast(pl.Float64),
    pl.col("angle_deg").cast(pl.Float64),
    pl.col("light_intensity_lux").cast(pl.Float64),
    pl.col("timestamp").str.strptime(pl.Datetime, strict=False)
])

df = df.filter(
    (pl.col("angle_deg") >= 0) &
    (pl.col("angle_deg") <= 90) &
    (pl.col("power_w") >= 0) &
    (pl.col("light_intensity_lux") >= 0)
)

df = df.drop_nulls()
df = df.unique()

df = df.with_columns([
    pl.col("weather").str.strip_chars().str.to_lowercase(),
    pl.col("room").str.strip_chars().str.to_lowercase()
])

df = df.with_columns([
    pl.when(pl.col("weather") == "suny")
    .then("sunny")
    .otherwise(pl.col("weather"))
    .alias("weather")
])

# ÚLOHA 3
df = df.with_columns(
    (pl.col("voltage_v") * pl.col("current_a")).alias("power_calc")
)

df = df.with_columns(
    (pl.col("power_calc") - pl.col("power_w")).alias("diff")
)

print(df.select("diff").describe())

# ÚLOHA 4
angle_analysis = df.group_by("angle_deg").agg(
    pl.col("power_w").mean()
)
print(angle_analysis)

# ÚLOHA 5
correlation = df.select(
    pl.corr("light_intensity_lux", "power_w")
)
print(correlation)

# ÚLOHA 6
environment = df.group_by("room").agg(
    pl.col("power_w").mean()
)
print(environment)

# ÚLOHA 7
best = df.sort("power_w", descending=True).head(5)
print(best)

# ÚLOHA 8
extreme_power = df.sort("power_w", descending=True).head(5)
extreme_lux = df.sort("light_intensity_lux", descending=True).head(5)

print(extreme_power)
print(extreme_lux)

# ÚLOHA 9
high_lux = df.filter(pl.col("light_intensity_lux") > 500)

analysis = high_lux.group_by("angle_deg").agg(
    pl.col("power_w").mean()
)

print(analysis)
