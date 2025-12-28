import numpy as np

def color_correction(rgb):
    """
    rgb: white-balanced image
    returns: color-corrected image
    """

    # Simple example color correction matrix
    ccm = np.array([
        [1.2, -0.1, -0.1],
        [-0.1, 1.2, -0.1],
        [-0.1, -0.1, 1.2]
    ])

    h, w, _ = rgb.shape
    reshaped = rgb.reshape(-1, 3)

    corrected = reshaped @ ccm.T

    return corrected.reshape(h, w, 3)

