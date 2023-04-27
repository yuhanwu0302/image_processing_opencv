import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img = Image.open("cards.png")

# Convert image to NumPy array
img_array = np.array(img)

# Create new image array with three copies of each pixel value
new_array = np.repeat(img_array[:, :, np.newaxis], 3, axis=2)

# Display new image
plt.imshow(new_array)
plt.show()
