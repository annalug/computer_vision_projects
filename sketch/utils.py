import cv2 as cv
from PIL import Image
import numpy as np

def sketch(image):
    ''' Function to sketch an image using OpenCV
    Args:
    image : fil
    '''
    # Convert image to grayscale


    img_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Clean up image using Guassian Blur
    img_gray_blur = cv.GaussianBlur(img_gray, (5 ,5), 0)

    # Extract edges
    canny_edges = cv.Canny(img_gray_blur, 20, 40)

    # Do an invert binarize the image
    ret, mask = cv.threshold(canny_edges, 70, 255, cv.THRESH_BINARY_INV)
    return mask

def show_pic(img):
    cv.imshow('Image', img)
    cv.waitKey(0)

    cv.destroyAllWindows()