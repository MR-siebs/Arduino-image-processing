import cv2 as cv
import numpy as np


def scan4laser(srcPath):

############ Retreiving base image #############

    src = cv.imread(srcPath)    # retreives source image

    img = cv.resize(src, (int(src.shape[1]/5), int(src.shape[0]/5)))    # resizes because the test image was to big :P

############ Image processing #############
    
    # cv.circle(img, maxLoc, 4, (255,00,00))

############ Showing images #############

    cv.imshow('source image', img)

    k = cv.waitKey(0)


# scan4laser("realDot.jpg")
