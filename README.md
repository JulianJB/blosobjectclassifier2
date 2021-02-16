# blosobjectclassifier2
`blosobjectclassifier2` is an upgraded, well-documented and fully in English version of the object classifier using computer vision developed as part of the internship program of the XXVII Scientific Research Summer at the CIC-IPN

## Dependencies

The following versions of the dependencies were used to run the object classifier under the PyCharm IDE. Similar versions of the dependencies will probably work but these have not been tested, whereas other major releases (such as downgrading to OpenCV 3 or Python 2) require changes to the code which are not within the scope of this documentation.

* `Python 3.8.0`
* `OpenCV 4.5.1.48`
* `pyttsx3 2.90`
* `Pillow 8.1.0`
* `NumPy 1.20.1`

## Deprecated dependencies

The following (estimated) versions of the dependencies were used in the original 2017 implementation of the object classifier that ran under the Spyder IDE. As the code has been updated these are no longer supported or documented in this version.
To see more about the legacy version of the object classifier visit the repository page of the project `blosobjectclassifier`

* `Python 3.x`
* `OpenCV 3.x`
* `pyttsx .x`
* `PIL .x`
* `NumPy 1.x`

## Installing the dependencies

By using the `pip` package installer from Python the project setup can be done very quickly from the terminal/console.
Run the following commands one by one to install all the required dependencies for the project:

`pip3 install opencv-python`

`pip3 install numpy`

`pip3 install pillow`

`pip3 install pyttsx3`

## Instructions for compiling

To run the object classifier, run from PyCharm or from the terminal/console:

`python3 training.py`

`python3 segmentation.py`

Changing the training/testing images with a command-line flag is currently not supported, therefore it has to be done manually from the code.
Future versions may implement this functionality.