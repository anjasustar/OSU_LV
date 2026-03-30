import pandas as pd

data = pd.read_csv('data_CO2_emission.csv')


print("Broj mjerenja:\n", len(data))

print("\nTipovi veličina:", data.dtypes)

print("\nIzostale veličine:", data.isnull().sum())

print("\nDuplicirane vrijednosti:", data.duplicated().sum())

data.dropna()
data.drop_duplicates()
data=data.reset_index(drop=True)

cat_cols = data.select_dtypes(include="object").columns
data[cat_cols] = data[cat_cols].astype("category")
print(data.dtypes)

print("\nNajveća gradska potrošnja:")
print(data.nlargest(3, 'Fuel Consumption City (L/100km)'))[['Make'], ['Model'], ['Fuel Consumption City (L/100km)']]

print("\nNajmanja gradska potrošnja:")
print(data.nsmallest(3, 'Fuel Consumption City (L/100km)'))[['Make'], ['Model'], ['Fuel Consumption City (L/100km)']]

result = data[(data['Engine Size(L)']>2.4)& (data['Engine Size(L)']<3.5)]
print("\nBroj vozila:", len(result))
print(result['CO2 Emissions (g/km)'].mean())

audi = data[data['Make'] == "Audi"]
print("\nBroj audi vozila:", len(audi))

result_audi = audi[(audi['Cylinders'] == 4)]
print(result_audi['CO2 Emissions (g/km)'].mean())

print("\nBroj vozila po cilindrima:")
print(data["Cylinders"].value_counts().sort_index())

print("\nProsječna CO2 emisija po cilindrima:")
print(data.groupby("Cylinders")["CO2 Emissions (g/km)"].mean())

diesel = data[data['Fuel Type'] == 'D']
gasoline = data[data['Fuel Type'] == 'X']

print("Broj diesel vozila:", len(diesel))
print("Broj vozila na regularnom benzinu:", len(gasoline))

print("\nProsječna gradska potrošnja (diesel):", diesel["Fuel Consumption City (L/100km)"].mean())
print("Medijan (diesel):", diesel["Fuel Consumption City (L/100km)"].median())

print("\nProsječna gradska potrošnja (regular):", gasoline["Fuel Consumption City (L/100km)"].mean())
print("Medijan (regular):", gasoline["Fuel Consumption City (L/100km)"].median())

diesel4 = data[(data["Cylinders"] == 4) & (data["Fuel Type"] == "D")].sort_values(by='Fuel Consumption City (L/100km)', ascending=False)
max = diesel4.head(1)

print("Automobil s 4 cilindra i dizelskim motorom koji ima najveću gradsku potrošnju: ")
print(max[['Make', 'Model', 'Fuel Consumption City (L/100km)']])

manual = data[data["Transmission"].str.contains("M")]
print("\nBroj manualnih vozila", len(manual))

print("Korelacija između numeričkih veličina: ")
print(data.corr(numeric_only=True))
