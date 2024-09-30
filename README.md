# Image Processing Project

This project focuses on image processing tasks using OpenCV in Python. It includes image manipulations like color conversion and simple image operations. The main file processes the famous 'Lena' image, demonstrating basic image processing techniques.

## Project Structure


## Requirements

- Python 3.x
- OpenCV
- Numpy

You can install the required libraries using the following command:

```bash
pip install opencv-python numpy

Alternatively, if you are using Conda, you can create the environment from the environment.yml file (if provided):
conda env create -f environment.yml
How to Run the Project
Clone the repository:
git clone https://github.com/your-username/image_processing.git
Navigate to the project directory:
cd image_processing
Run the Python script:
python rgb_to_bgr.py
The script will load the lena.jpg image, convert its color space from RGB to BGR, and display the result.

Explanation of the Code
rgb_to_bgr.py
This script reads an image and converts its color from RGB to BGR using OpenCV.

import cv2

# Load the image
image = cv2.imread('lena.jpg')

# Convert RGB to BGR
bgr_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Display the result
cv2.imshow('BGR Image', bgr_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
lena.jpg
The Lena image is a famous test image used in image processing tasks. It is included in the project for demonstration purposes.
