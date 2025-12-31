from raw_io import load_raw
from demosaic import demosaic
from white_balance import white_balance
from color_correction import color_correction
from tone_mapping import tone_map

import imageio.v3 as iio
import numpy as np

# 1) Load raw sensor data
bayer, pattern = load_raw("raw-photos/example_1.CR3")

# 2) Demosaic (get RGB everywhere)
rgb = demosaic(bayer, pattern)

# Display-ready checkpoint
iio.imwrite("demosaiced.png", (tone_map(rgb.copy()) * 255).astype(np.uint8))

# 3) White balance
rgb = white_balance(rgb)

# Display-ready checkpoint
iio.imwrite("white_balanced-2.png", (tone_map(rgb.copy()) * 255).astype(np.uint8))

# 4) Color correction
rgb = color_correction(rgb)

# Debug: display-ready color-corrected image before tone mapping
iio.imwrite("color_corrected_before_tone.png", (tone_map(rgb.copy()) * 255).astype(np.uint8))

# 5) Tone mapping / gamma
rgb = tone_map(rgb)

# 6) Save final image
iio.imwrite("final-3.png", (rgb * 255).astype(np.uint8))

