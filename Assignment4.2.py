import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
url = "https://vw4.viope.com/content/227e2e3690ca144891b51d8664d3a84a2edafc2c/weight-height(1).csv"
df = pd.read_csv(url)
X = df[['Height']].values
y = df['Weight'].values
plt.scatter(X, y, color='blue', alpha=0.5)
plt.xlabel("Height (inches)")
plt.ylabel("Weight (pounds)")
plt.title("Height vs. Weight")
plt.show()
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)
plt.scatter(X, y, color='blue', alpha=0.5)
plt.plot(X, y_pred, color='red', linewidth=2)
plt.xlabel("Height (inches)")
plt.ylabel("Weight (pounds)")
plt.title("Regression Line: Height vs. Weight")
plt.show()
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print(f"Root Mean Square Error (RMSE): {rmse:.2f}")
print(f"R² Score: {r2:.4f}")