try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
except ModuleNotFoundError as e:
    print(f"Missing library: {e.name}. Please install it by running 'pip install {e.name}' in your terminal.")
    exit()

try:
    data = pd.read_csv('weight-height.csv')  # Replace with the full path to your CSV file if needed
except FileNotFoundError:
    print("Error: The file 'weight-height.csv' was not found. Ensure it is in the correct directory.")
    exit()

if 'Height' not in data.columns or 'Weight' not in data.columns:
    print("Error: The CSV file must contain 'Height' and 'Weight' columns.")
    exit()

length = data['Height'].values  # Heights in inches
weight = data['Weight'].values  # Weights in pounds

length_cm = length * 2.54
weight_kg = weight * 0.453592

mean_length_cm = np.mean(length_cm)
mean_weight_kg = np.mean(weight_kg)

print(f"Mean Length (cm): {mean_length_cm:.2f}")
print(f"Mean Weight (kg): {mean_weight_kg:.2f}")

plt.hist(length_cm, bins=20, color='blue', edgecolor='black')
plt.title('Histogram of Lengths (in cm)')
plt.xlabel('Length (cm)')
plt.ylabel('Frequency')
plt.show()