import numpy as np

def white_balance(rgb):
    """
    rgb: H x W x 3 image after demosaicing
    returns: white-balanced RGB
    """

    # Average brightness of each color
    r_mean = np.mean(rgb[:, :, 0])
    g_mean = np.mean(rgb[:, :, 1])
    b_mean = np.mean(rgb[:, :, 2])

    # Target each channel toward the overall gray level to avoid green bias
    target = (r_mean + g_mean + b_mean) / 3.0
    eps = 1e-8
    gains = np.array([
        target / (r_mean + eps),
        target / (g_mean + eps),
        target / (b_mean + eps),
    ], dtype=rgb.dtype)

    # Stronger green reduction so the change is clearly visible; tweak as needed
    green_adjust = 0.7
    gains *= np.array([1.0, green_adjust, 1.0], dtype=rgb.dtype)

    return rgb * gains

