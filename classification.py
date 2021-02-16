"""
@class: classification.py
@author: Julian Blos
"""

import math
import numpy as np


def classify(first_hu):
    # Defining the class representatives
    representatives = [2.7911, 3.1498, 2.6037, 2.2882, 3.0371]

    # Get the first Hu moment invariant of the image
    img_moment = first_hu

    # Calculate the distance for each class
    dist = []
    for i in range(len(representatives)):
        dist.append(round(math.sqrt(
            math.pow((img_moment - representatives[i]), 2)), 4))

    # Print the class representatives, the first Hu moment invariant, and
    # the distances (for debugging purposes).
    print('Class representatives: ', representatives)
    print('First Hu moment invariant: ', img_moment)
    print('Distances: ', dist)

    # Get the minimum distance from the object classes
    argmin = np.argmin(dist)
    argvalue = dist[argmin]

    # Get the corresponding class from which the object in the image belongs
    obj_class = argmin + 1

    # Print the minimum distance value
    print('The minimum distance value is (argmin): ', argmin)
    print('The value of argvalue is: ', argvalue)

    # Print the class to which the object in the image belongs
    print('Class: ', obj_class)

    return obj_class
