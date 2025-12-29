import rawpy
import numpy as np
import imageio.v3 as iio


def load_raw(path="raw-photos/example_1.CR3"):
    """
    Load RAW Bayer data and normalize to [0, 1].
    Returns (bayer, pattern).
    """
    with rawpy.imread(path) as raw:
        # Extract visible Bayer sensor data
        bayer = raw.raw_image_visible.astype(np.float32)

        # Get black and white levels
        black = np.mean(raw.black_level_per_channel)
        white = raw.white_level

        # Normalize to [0, 1]
        bayer = np.clip((bayer - black) / (white - black), 0, 1)

        # Bayer pattern (RGGB, etc.)
        pattern = raw.raw_pattern

    # Save Bayer image just to inspect it
    iio.imwrite("bayer_debug.png", (bayer * 255).astype(np.uint8))

    return bayer, pattern

