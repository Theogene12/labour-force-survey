import matplotlib.pyplot as plt
import numpy as np

# Generate a random dataset
data = np.random.randn(1000)

# Create a histogram using Matplotlib
plt.hist(data, bins=20, color='blue', alpha=0.7, rwidth=0.85)
plt.xlabel('X-axis label')
plt.ylabel('Frequency')
plt.title('Histogram Example (Matplotlib)')
plt.grid(True)
plt.show()
