# ============================================
# Arrhenius analysis for kinetic constants
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# --------------------------------------------
# Temperatures (°C → K)
# --------------------------------------------
T_C = np.array([20, 30, 40, 50])
T_K = T_C + 273.15

# --------------------------------------------
# Replace these with your fitted constants
# Example: using k1 (PFO) or k2 (PSO)
# --------------------------------------------
# Can COPY from your results_df or manually

k_values = np.array([
    0.xxx,  # 20 °C
    0.xxx,  # 30 °C
    0.xxx,  # 40 °C
    0.xxx   # 50 °C
])

# --------------------------------------------
# Arrhenius linearization
# --------------------------------------------
inv_T = 1 / T_K
ln_k = np.log(k_values)

# Linear regression
slope, intercept, r_value, p_value, std_err = linregress(inv_T, ln_k)

# Constants
R = 8.314  # J/mol·K

Ea = -slope * R        # Activation energy (J/mol)
A = np.exp(intercept)  # Pre-exponential factor

# --------------------------------------------
# Print results
# --------------------------------------------
print("\nArrhenius analysis results:")
print(f"Activation energy (Ea): {Ea/1000:.2f} kJ/mol")
print(f"Pre-exponential factor (A): {A:.4e}")
print(f"R²: {r_value**2:.4f}")

# --------------------------------------------
# Plot Arrhenius
# --------------------------------------------
plt.figure(figsize=(6,5))

plt.scatter(inv_T, ln_k, label='Data')
plt.plot(inv_T, slope*inv_T + intercept, '--', label='Fit')

plt.xlabel('1/T (1/K)')
plt.ylabel('ln(k)')
plt.title('Arrhenius plot')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()