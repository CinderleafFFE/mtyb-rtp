from PIL import Image
import numpy as np
# Checks if two bitmaps are equal by virtue
# i.e. for alpha-channeled bitmaps, all A=0 pixels are identified regardless of RGB
def check_equal_virtue(fn1, fn2):
    im1 = Image.open(fn1)
    im2 = Image.open(fn2)
    
    # Don't process if two images have different channels
    if im1.mode != im2.mode:
        return False
    # Nor process if channel mode is other than 8bit grayscale, true color or w/ alpha
    good_modes = ["RGB", "RGBA", "L"]
    if not im1.mode in good_modes:
        return False
    im1_arr = np.array(im1)
    if im1_arr.dtype != np.dtype('uint8'):
        return False
    im2_arr = np.array(im2)

    im1.close()
    im2.close()

    # Identify transparent pixels
    if im1.mode == "RGBA":
        # Normalize RGB to zero if A is zero
        im1_alpha_nonzero = np.minimum(im1_arr[:, :, 3], 1)
        im1_arr[:, :, 0] *= im1_alpha_nonzero
        im1_arr[:, :, 1] *= im1_alpha_nonzero
        im1_arr[:, :, 2] *= im1_alpha_nonzero
        im2_alpha_nonzero = np.minimum(im2_arr[:, :, 3], 1)
        im2_arr[:, :, 0] *= im2_alpha_nonzero
        im2_arr[:, :, 1] *= im2_alpha_nonzero
        im2_arr[:, :, 2] *= im2_alpha_nonzero

    if np.array_equal(im1_arr, im2_arr):
        return True
    else:
        return False
