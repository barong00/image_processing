import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = "C:/Users/boran/Desktop/Dosyalar/python/image_processing/lena.jpg"

image = cv2.imread(image_path)

# Read the image using OpenCV (in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Separate the RGB channels
blue_channel = image_rgb[:, :, 0]
green_channel = image_rgb[:, :, 1]         
red_channel = image_rgb[:, :, 2]

# Apply the Sobel filter to the blue channel in both x and y directions
sobel_xy_blue = cv2.Sobel(blue_channel, cv2.CV_64F, 1, 1, ksize=3)

sobel_xy_green = cv2.Sobel(green_channel, cv2.CV_64F, 1, 1, ksize=3)

sobel_xy_red = cv2.Sobel(red_channel, cv2.CV_64F, 1, 1, ksize=3)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary thresholding to the grayscale image
(thresh, output2) = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
output2 = cv2.GaussianBlur(output2, (5, 5), 3)


# Perform Canny edge detection on each color channel
canny_output = cv2.Canny(output2, 180, 255)
Canny_red = cv2.Canny(red_channel, 180, 255)
Canny_blue = cv2.Canny(blue_channel, 180, 255)
Canny_green = cv2.Canny(green_channel, 180, 255)

# Compute the edge magnitude for each channel (used for visualization)
edge_magnitude_blue = np.sqrt(sobel_xy_blue**2 + sobel_xy_blue**2)
edge_magnitude_green = np.sqrt(sobel_xy_green**2 + sobel_xy_green**2)
edge_magnitude_red = np.sqrt(sobel_xy_red**2 + sobel_xy_red**2)



canny_output_rgb = cv2.cvtColor(canny_output, cv2.COLOR_GRAY2RGB)

# Create a figure to display the results
plt.figure(figsize=(12,8))

plt.subplot(331)
plt.imshow(red_channel, cmap='gray')
plt.title('Red Channel')
plt.axis('off')

plt.subplot(334)
plt.imshow(Canny_red, cmap='gray')
plt.title('Canny Red Channel')
plt.axis('off')

plt.subplot(337)
plt.imshow(cv2.convertScaleAbs(sobel_xy_red), cmap='gray')
plt.title('Sobel Red Channel')
plt.axis('off')


plt.subplot(332)
plt.imshow(green_channel, cmap='gray')
plt.title('Green Channel')
plt.axis('off')

plt.subplot(335)
plt.imshow(Canny_green, cmap='gray')
plt.title('Canny Green Channel')
plt.axis('off')

plt.subplot(338)
plt.imshow(cv2.convertScaleAbs(sobel_xy_green),cmap='gray')
plt.title('Sobel Green Channel')
plt.axis('off')


plt.subplot(333)
plt.imshow(blue_channel, cmap='gray')
plt.title('Blue Channel')
plt.axis('off')

plt.subplot(336)
plt.imshow(Canny_blue, cmap='gray')
plt.title('Canny Blue Channel')
plt.axis('off')

plt.subplot(339)
plt.imshow(cv2.convertScaleAbs(sobel_xy_blue),cmap='gray')
plt.title('Sobel Blue Channel')
plt.axis('off')



plt.tight_layout()
plt.show()

