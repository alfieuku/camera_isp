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

    # Scale so all channels match green
    rgb[:, :, 0] *= g_mean / r_mean
    rgb[:, :, 2] *= g_mean / b_mean

    return rgb

