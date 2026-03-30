import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("D:/osu_lv/LV3/data_C02_emission.csv")

plt.figure()

plt.hist(data["CO2 Emissions (g/km)"], bins=30)

plt.xlabel("CO2 Emissions (g/km)")
plt.ylabel("Broj vozila")
plt.title("Histogram emisije CO2")

plt.show()

plt.figure()

fuel_types = data["Fuel Type"].unique()

for fuel in fuel_types:
    subset = data[data["Fuel Type"] == fuel]
    plt.scatter(
        subset["Fuel Consumption City (L/100km)"],
        subset["CO2 Emissions (g/km)"],
        label=fuel
    )

plt.xlabel("Gradska potrošnja (L/100km)")
plt.ylabel("CO2 emisija (g/km)")
plt.title("Odnos gradske potrošnje i CO2 emisije")

plt.legend()

plt.show()


plt.figure()

data.boxplot(column = "Fuel Consumption Hwy (L/100km)", by = "Fuel Type")
plt.xlabel("Tip goriva")
plt.ylabel("Izvangradska potrošnja (L/100km)")
plt.title("Izvangradska potrošnja prema tipu goriva")

plt.show()


fuel_counts = data.groupby("Fuel Type").size()

plt.figure()

plt.bar(fuel_counts.index, fuel_counts.values)

plt.xlabel("Tip goriva")
plt.ylabel("Broj vozila")
plt.title("Broj vozila po tipu goriva")

plt.show()


avg_co2 = data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean()

plt.figure()

plt.bar(avg_co2.index, avg_co2.values)

plt.xlabel("Broj cilindara")
plt.ylabel("Prosječna CO2 emisija (g/km)")
plt.title("Prosječna CO2 emisija prema broju cilindara")

plt.show()
