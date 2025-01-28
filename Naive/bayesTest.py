import numpy as np

def coin_flip_simulation(n_flips):
    flips = np.random.binomial(n=1, p=0.5, size=n_flips)
    return np.mean(flips)

# Simulate 1000 flips
result = coin_flip_simulation(100000000)
print(f"Proportion of heads: {result}")