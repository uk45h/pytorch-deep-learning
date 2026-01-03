import torch
import matplotlib.pyplot as plt
import numpy as np

# 1. Tworzymy dane wejściowe (oś X)
x = torch.linspace(-5, 5, 100).reshape(-1, 1)

# 2. Definiujemy 5 neuronów (ręcznie dobrane wagi i biasy dla czytelności)
# Wagi (nachylenie linii)
weights = torch.tensor([[1.5, 0.8, -1.2, -0.5, 2.0]])
# Biasy (przesunięcie linii lewo/prawo)
biases = torch.tensor([[-2.0, 1.0, 0.5, -1.5, 2.0]])

# 3. Przejście przez warstwę Linear: y = x * w + b
z = x @ weights + biases

# 4. Przejście przez ReLU: max(0, z)
a = torch.relu(z)

# 5. Sumowanie (to co robi kolejna warstwa)
summed = torch.sum(a, dim=1)

# --- WIZUALIZACJA ---
plt.figure(figsize=(15, 5))

# Wykres 1: Same linie (Linear)
plt.subplot(1, 3, 1)
plt.plot(x, z)
plt.title("1. Warstwa Linear\n(5 prostych linii)")
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', lw=1)

# Wykres 2: Po ReLU
plt.subplot(1, 3, 2)
plt.plot(x, a)
plt.title("2. Po ReLU\n(Ucięcie wszystkiego < 0)")
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', lw=1)

# Wykres 3: Efekt końcowy (Suma w 2. warstwie)
plt.subplot(1, 3, 3)
plt.plot(x, summed, color='red', lw=3)
plt.title("3. Wynik (Połączenie cech)\n(Złożony, nieliniowy kształt)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()