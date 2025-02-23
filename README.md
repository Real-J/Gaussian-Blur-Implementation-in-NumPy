# Gaussian Blur Implementation in NumPy

This project implements **Gaussian Blur** manually using **NumPy** without relying on external libraries like SciPy or OpenCV. The script converts an image to grayscale and applies a Gaussian blur filter using a manually defined kernel and convolution.

## Features
- Converts an image to grayscale manually.
- Defines a Gaussian kernel without external libraries.
- Performs convolution manually using NumPy.
- Displays the original grayscale and blurred images using Matplotlib.

## Prerequisites
Ensure you have **Python 3.x** installed along with the following libraries:

```bash
pip install numpy matplotlib
```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Real-J/gaussian-blur-numpy.git
   cd gaussian-blur-numpy
   ```
2. Place your image in the project directory.
3. Modify the script to provide the correct image path:
   ```python
   image = plt.imread("path/to/your/image.jpg")
   ```
4. Run the script:
   ```bash
   python gaussian_blur.py
   ```

## Code Explanation
### 1. Load and Convert Image to Grayscale
The image is loaded using Matplotlib and converted to grayscale manually:
```python
image = plt.imread("path/to/image.jpg")
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
```

### 2. Define Gaussian Kernel
A Gaussian kernel is created using NumPy:
```python
size = 5
sigma = 1.0
ax = np.linspace(-(size // 2), size // 2, size)
gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
kernel = np.outer(gauss, gauss)
kernel /= np.sum(kernel)
```

### 3. Apply Convolution
Instead of using SciPy, convolution is performed manually:
```python
pad_size = size // 2
padded_image = np.pad(gray_image, pad_size, mode='reflect')
blurred_image = np.zeros_like(gray_image)

for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        blurred_image[i, j] = np.sum(padded_image[i:i+size, j:j+size] * kernel)
```

### 4. Display Results
The grayscale and blurred images are displayed using Matplotlib:
```python
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(gray_image, cmap="gray")
ax[0].set_title("Grayscale Image")
ax[1].imshow(blurred_image, cmap="gray")
ax[1].set_title("Blurred Image")
plt.show()
```

## Optimization Suggestions
- **Vectorized Convolution**: Instead of nested loops, use NumPy slicing to speed up the convolution process.
- **Use SciPy for Faster Convolution**: Replace manual convolution with `scipy.ndimage.convolve` for efficiency.

## License
This project is open-source and available under the MIT License.

---
### 🔥 Contributions Welcome!
Feel free to fork the repo, submit pull requests, or report issues!

