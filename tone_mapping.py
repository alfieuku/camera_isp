import numpy as np

def tone_map(rgb, exposure=4.5):
    """
    rgb: color-corrected image (values around 0–1)
    returns: display-ready image
    """

    # 1) Apply exposure gain then clamp
    rgb = np.clip(rgb * exposure, 0, 1)

    # 2) Apply simple gamma (make it brighter for display)
    gamma = 1 / 2.2
    rgb = rgb ** gamma

    return rgb

