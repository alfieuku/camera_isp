import numpy as np

def demosaic(bayer, pattern):
    h, w = bayer.shape
    rgb = np.zeros((h, w, 3), dtype=np.float32)

    # ---- STEP 1: place known values (assume RGGB) ----
    rgb[0::2, 0::2, 0] = bayer[0::2, 0::2]  # Red
    rgb[0::2, 1::2, 1] = bayer[0::2, 1::2]  # Green
    rgb[1::2, 0::2, 1] = bayer[1::2, 0::2]  # Green
    rgb[1::2, 1::2, 2] = bayer[1::2, 1::2]  # Blue

    # ---- STEP 2: fill missing values by simple averaging ----
    for c in range(3):  # for R, G, B
        channel = rgb[:, :, c]
        mask = channel == 0

        # very simple neighbor average
        channel[mask] = (
            np.roll(channel, 1, axis=0)[mask] +
            np.roll(channel, -1, axis=0)[mask] +
            np.roll(channel, 1, axis=1)[mask] +
            np.roll(channel, -1, axis=1)[mask]
        ) / 4

        rgb[:, :, c] = channel

    return rgb
