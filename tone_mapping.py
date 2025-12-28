import numpy as np

def tone_map(rgb):
    """
    rgb: color-corrected image (values around 0–1)
    returns: display-ready image
    """

    # 1) Clamp to valid range
    rgb = np.clip(rgb, 0, 1)

    # 2) Apply simple gamma (make it brighter for display)
    gamma = 1 / 2.2
    rgb = rgb ** gamma

    return rgb

