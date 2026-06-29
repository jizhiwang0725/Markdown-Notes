import numpy as np
import matplotlib.pyplot as plt

def create_gabor_filter(size, sigma, theta, frequency):
    # 1. Create a 2D pixel grid (X and Y coordinates)
    x, y = np.meshgrid(np.linspace(-size/2, size/2, size), 
                       np.linspace(-size/2, size/2, size))
    
    # 2. Rotate the grid coordinates based on our desired angle (theta)
    x_theta = x * np.cos(theta) + y * np.sin(theta)
    
    # 3. Step One: The Gaussian Envelope (The bounding bell curve)
    # This creates a soft circle that fades out from the center
    gaussian = np.exp(-(x**2 + y**2) / (2 * sigma**2))
    
    # 4. Step Two: The Cosine Wave (The alternating stripes)
    # We apply the wave along the rotated x-axis (x_theta)
    cosine = np.cos(2 * np.pi * frequency * x_theta)
    
    # 5. Step Three: Multiply them together!
    gabor = gaussian * cosine
    
    return gabor, gaussian, cosine

# --- Set your parameters here ---
grid_size = 100        # Make a 100x100 pixel canvas
sigma = 15.0           # Size of the bell curve boundary
theta = np.pi / 4      # Angle of the stripes (45 degrees in radians)
frequency = 0.05       # How tightly packed the stripes are

# Generate the math
gabor_final, gaussian_env, cosine_wave = create_gabor_filter(grid_size, sigma, theta, frequency)

# --- Plot the results ---
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Plot the infinite stripes
axes[0].imshow(cosine_wave, cmap='gray')
axes[0].set_title("1. The Cosine Wave (Infinite Stripes)")

# Plot the bounding circle
axes[1].imshow(gaussian_env, cmap='gray')
axes[1].set_title("2. The Gaussian Envelope (Boundary)")

# Plot the final multiplied result
axes[2].imshow(gabor_final, cmap='gray')
axes[2].set_title("3. Final Gabor Filter (Multiplied)")

for ax in axes:
    ax.axis('off') # Hide the axes ticks for a cleaner image

plt.tight_layout()
plt.show()