import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file
mat = scipy.io.loadmat('/content/240819_EH_01_01_100_qs.mat')

# Show available keys
print("Available keys:", mat.keys())

# Load the actual variable
data = mat['img_qs']
print(f"\nLoaded variable: img_qs")
print("Original data shape:", data.shape)

# Remove singleton dimensions
data = np.squeeze(data)
print("Squeezed data shape:", data.shape)

# Handle non-finite values by replacing them with a small positive number
data[~np.isfinite(data)] = 1e-9

# Apply log compression
# Add a small constant to avoid log(0) - np.log1p already handles the +1
data_compressed = np.log1p(data)
print("Applied log compression.")

# Plot the last frame if 3D
if data_compressed.ndim == 3:
    plt.imshow(data_compressed[:, :, -1], cmap='jet')
    plt.show()
else:
    print("Data is not 3D after squeezing.")
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Load the .mat file
mat = scipy.io.loadmat('/content/240819_EH_01_01_100_qs.mat')

# Show available keys
print("Available keys:", mat.keys())

# Load the actual variable
data = mat['img_qs']
print(f"\nLoaded variable: img_qs")
print("Original data shape:", data.shape)

# Remove singleton dimensions
data = np.squeeze(data)
print("Squeezed data shape:", data.shape)

# Handle non-finite values by replacing them with a small positive number
data[~np.isfinite(data)] = 1e-9

# Apply log compression
# Add a small constant to avoid log(0) - np.log1p already handles the +1
data_compressed = np.log1p(data)
print("Applied log compression.")

# Plot the last frame if 3D
if data_compressed.ndim == 3:
    plt.imshow(data_compressed[:, :, -1], cmap='jet')
    plt.show()
else:
    print("Data is not 3D after squeezing.")
