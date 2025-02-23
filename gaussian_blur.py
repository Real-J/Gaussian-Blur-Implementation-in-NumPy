import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = plt.imread("codename47")  # Replace with actual path

# Convert to grayscale manually
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Define Gaussian kernel manually
size = 5
sigma = 1.0
ax = np.linspace(-(size // 2), size // 2, size)
gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
kernel = np.outer(gauss, gauss)
kernel /= np.sum(kernel)  # Normalize the kernel

# Padding
pad_size = size // 2
padded_image = np.pad(gray_image, pad_size, mode='reflect')

# Apply convolution manually
blurred_image = np.zeros_like(gray_image)
for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        blurred_image[i, j] = np.sum(padded_image[i:i+size, j:j+size] * kernel)

# Display images
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(gray_image, cmap="gray")
ax[0].set_title("Grayscale Image")
ax[0].axis("off")

ax[1].imshow(blurred_image, cmap="gray")
ax[1].set_title("Blurred Image")
ax[1].axis("off")

plt.show()
