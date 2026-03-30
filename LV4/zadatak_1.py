import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


#a zadatak
df = pd.read_csv("data_C02_emission.csv")

features = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)"]
X = df[features]
y = df["CO2 Emissions (g/km)"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# b zadatak
plt.scatter(X_train["Engine Size (L)"], y_train, color="blue", label="Train")
plt.scatter(X_test["Engine Size (L)"], y_test, color="red", label="Test")

plt.xlabel("Engine Size (L)")
plt.ylabel("CO2 Emissions (g/km)")
plt.legend()
plt.title("Ovisnost emisije CO2 o veličini motora")

plt.show()


# c zadatak
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

plt.hist(X_train["Engine Size (L)"], bins=20)
plt.title("Prije skaliranja")
plt.show()

plt.hist(X_train_scaled[:, 0], bins=20)
plt.title("Nakon skaliranja")
plt.show()


#d zadatak
df = pd.read_csv("data_C02_emission.csv")

features = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)"]
X = df[features]
y = df["CO2 Emissions (g/km)"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LinearRegression()
model.fit(X_train_scaled, y_train)

print("Parametri modela:")
print("θ0 (intercept):", model.intercept_)

for i, coef in enumerate(model.coef_):
    print(f"θ{i+1} (za {features[i]}):", coef)

print("\nModel (izraz 4.6):")
equation = f"y = {model.intercept_:.4f}"
for i, coef in enumerate(model.coef_):
    equation += f" + ({coef:.4f}) * x{i+1}"
print(equation)


#e zadatak
y_pred = model.predict(X_test_scaled)

plt.scatter(y_test, y_pred)
plt.xlabel("Stvarne vrijednosti")
plt.ylabel("Predviđene vrijednosti")
plt.title("Stvarno vs Predviđeno")

plt.show()

#f zadatak
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("MAE:", mae)
print("R2:", r2)
