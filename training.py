"""
@class: training.py
@author: Julian Blos
"""

from PIL import Image
import numpy as np
import glob
import cv2

# A constant value to distinguish between the noisy images
# and the non-noisy images from the dataset.
avg_color_value = 90

# A cumulative variable to calculate the average of the
# Hu moment invariants from the image dataset.
accum = 0

# A variable to store the path of the image dataset

# Image dataset #01 (class Screw)
file_set = 'training/IMAG01*.BMP'

# Image dataset #02 (class Washer)
# file_set = 'training/IMAG02*.BMP'

# Image dataset #03 (class Screw Eye)
# file_set = 'training/IMAG03*.BMP'

# Image dataset #04 (class Tenterhook)
# file_set = 'training/IMAG04*.BMP'

# Image dataset #01 (class Dovetail)
# file_set = 'training/IMAG05*.BMP'

# A file list for the image dataset
file_list = glob.glob(file_set)

# An array for the files of the image dataset
img_arr = np.array([np.array(Image.open(file_name))
                    for file_name in file_list])

# Iterate over all the images in the dataset
for i in range(len(img_arr)):

    # Read the image from the dataset
    image = cv2.imread(file_list[i])

    # Show the image from the dataset
    cv2.imshow("Original", image)

    # Calculate the average color value of the image
    avg_color_per_row = np.average(image, axis=(0, 1))
    avg_color = np.average(avg_color_per_row, axis=0)
    avg_color = int(round(avg_color))

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Determine the level of noise present in the image
    if avg_color > avg_color_value:
        # The image is too noisy, discard the image
        print(avg_color)
    else:
        # Apply a distortion filter (median blur)
        blurred = cv2.medianBlur(gray, 7)

        # Show the blurred image
        cv2.imshow("Blurred", blurred)

        # Apply a manual threshold of 90
        (T, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

        # Show the thresholded image
        cv2.imshow("Thresholded", thresh)

    # Calculate the image moments of the thresholded image
    img_moments = cv2.moments(thresh)

    # Calculate the Hu moment invariants from the image moments
    hu_moments = cv2.HuMoments(img_moments)

    # Get the first Hu moment invariant
    first_hu = -np.sign(hu_moments[0]) * np.log10(np.abs(hu_moments[0]))

    # Store the value of the first Hu moment invariant into the cumulative variable
    accum += first_hu

# Calculate the average value of the first Hu moment invariant for the image dataset
avg_image_set = np.round(accum / 10, 4)

# Print the cumulative value for each image dataset (for debugging purposes)
accum = np.round(accum, 4)
print('Cumulative: ', accum)

# Print the average value of the image dataset
print('Average value: ', avg_image_set)

cv2.waitKey(0)
