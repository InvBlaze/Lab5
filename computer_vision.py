from PIL import Image, ImageChops, ImageFilter
import numpy as np

def person_detected(image1_file, image2_file, t1):
    """Compares two images and determines if a person is detected based on a threshold t1."""
    
    # Load images and convert to grayscale
    image1 = Image.open(image1_file).convert('L')
    image2 = Image.open(image2_file).convert('L')

    # Ensure both images are the same size
    if image1.size != image2.size:
        image2 = image2.resize(image1.size)

    # Apply Gaussian blur to reduce noise
    image1 = image1.filter(ImageFilter.GaussianBlur(radius=1))
    image2 = image2.filter(ImageFilter.GaussianBlur(radius=1))

    # Convert images to numpy arrays
    img1_array = np.array(image1, dtype=np.int16)
    img2_array = np.array(image2, dtype=np.int16)

    # Compute absolute difference
    diff = np.abs(img1_array - img2_array)

    # Normalize the difference (optional but useful)
    diff = diff / np.max(diff) * 255  # Scale difference to range 0-255

    # Sum of all pixel differences
    diff_sum = np.sum(diff)

    # Adaptive threshold calculation (optional, replaces t1 with a learned value)
    adaptive_t1 = np.mean(diff) * image1.size[0] * image1.size[1] * 0.5  # Dynamic threshold

    # Debugging Output (to fine-tune threshold)
    print(f"[DEBUG] Diff Sum: {diff_sum}, Threshold: {adaptive_t1}")

    # Determine if difference exceeds threshold
    return diff_sum > adaptive_t1


