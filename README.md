Project to solidify understanding of image signal processing with a raw image. Files below:

1. raw_io.py - processing raw data and extracting bayer pattern
2. demosaic.py - taking pixel data with single color pixel values and averaging surrounding values to make three values per pixel
3. white_balance.py - taking green pixel values and matching its average with red and blue to fix lighting problems
4. color_correction.py - adjusting errors in sensor values per color
5. tone_mapping.py - converting pixel values to display ready values
6. main.py - running pipeline and saving image checkpoints for each stage
