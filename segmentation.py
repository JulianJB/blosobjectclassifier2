"""
@class: segmentation.py
@author: Julian Blos
"""

from classification import classify
import numpy as np
import pyttsx3
import cv2

# Setting up the text-to-speech engine
tts_engine = pyttsx3.init()
tts_rate = tts_engine.getProperty('rate')

# Open the image from the testing dataset
image = cv2.imread('testing/IMAG111.BMP')

# Show the image from the testing dataset
cv2.imshow("Original", image)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a distortion filter (median blur)
blurred = cv2.medianBlur(gray, 7)

# Show the blurred image
cv2.imshow("Blurred", blurred)

# Apply a manual threshold of 90
(T, thresh) = cv2.threshold(blurred, 90, 255, cv2.THRESH_BINARY)

# Show the thresholded image
cv2.imshow("Thresholded", thresh)

# Labeling the connected components within the frame
# Get the connected components of the thresholded image
components = cv2.connectedComponentsWithStats(thresh, 4, cv2.CV_32S)

# Number of labels of the connected components
num_labels = components[0]

# Labels of the connected components
labels = components[1]

# Stats of the connected components
stats = components[2]

# Centroids of the connected components
centroids = components[3]

# For every label in the image
for label in range(num_labels):

    # Ignore the first label as this corresponds to the image background
    if label == 0:
        continue

    # Dimensions for the Region of Interest (ROI)
    # Get the width of the bounding box of the connected component
    width = stats[label, cv2.CC_STAT_WIDTH]

    # Get the height of the bounding box of the connected component
    height = stats[label, cv2.CC_STAT_HEIGHT]

    # Get the leftmost coordinate of the bounding box of the connected component
    x = stats[label, cv2.CC_STAT_LEFT]

    # Get the upmost coordinate of the bounding box of the connected component
    y = stats[label, cv2.CC_STAT_TOP]

    # Creating the ROI of the connected component
    roi = thresh[y:y + height, x:x + width]

    # Calculating the image moments of the ROI
    img_moments = cv2.moments(roi)

    # Calculating the Hu moment invariants of the ROI
    hu = cv2.HuMoments(img_moments)

    # Obtaining the first Hu moment invariant
    firstHu = -np.sign(hu[0]) * np.log10(np.abs(hu[0]))

    # Get the class of the corresponding connected component
    obj_class = (clasificar(np.round(firstHu, 4)))

    # Types of object classes
    # Associate a color and a label to the object class of the connected component
    if obj_class == 1:
        classLabel = "screw"
        color = (255, 0, 0)  # the color for the contour of the object class
    elif obj_class == 2:
        classLabel = "washer"
        color = (0, 255, 0)
    elif obj_class == 3:
        classLabel = "screw eye"
        color = (0, 0, 255)
    elif obj_class == 4:
        classLabel = "tenterhook"
        color = (0, 255, 255)
    else:
        classLabel = "dovetail"
        color = (255, 255, 0)

    # Dimensions for labeling from the coordinates of the centroid
    # of the component in X and Y.
    # Calculating the coordinate in X of the centroid of the component
    cX = int(centroids[label, 0])

    # Calculating the coordinate in Y of the centroid of the component
    cY = int(centroids[label, 1])

    # Add the corresponding label according to the class of the component
    cv2.putText(image, classLabel, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, color, 2)

    # Finding the contours of the ROI
    contours = cv2.findContours(roi.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

    # Prepare the contours as required by OpenCV 4
    contours = contours[0]

    # Iterate according to the number of contours
    for c in contours:
        # Draw the contours for the objects in the image
        cv2.drawContours(image, [c], -1, color, 2, offset=(x, y))

        # Show the image from the testing dataset correctly classified
        cv2.imshow("Result", image)

        # Perform the speech by saying the corresponding label for the object
        # pyttsx3 speech temporarily disabled due to a bug in MacOS, see:
        # https://stackoverflow.com/questions/27338298/workaround-for-pyttsx-engine-runandwait-not-returning-on-yosemite
        # tts_engine.say(classLabel)
        # tts_engine.runAndWait()

        cv2.waitKey(0)
