import numpy as np

def color_correction(rgb):
    """
    rgb: white-balanced image
    returns: color-corrected image
    """

    # Simple example color correction matrix
    ccm = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ])

    h, w, _ = rgb.shape
    reshaped = rgb.reshape(-1, 3)

    corrected = reshaped @ ccm.T
    corrected = np.clip(corrected, 0.0, 1.0)

    return corrected.reshape(h, w, 3)

