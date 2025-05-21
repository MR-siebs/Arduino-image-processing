import cv2 as cv
import numpy as np


def scan4laser(srcPath):

############ Retreiving base image #############

    src = cv.imread(srcPath)    # retreives source image

    img = cv.resize(src, (int(src.shape[1]/5), int(src.shape[0]/5)))    # resizes because the test image was to big :P

############ Image processing #############

    imgGray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(imgGray)
    
    # cv.circle(img, maxLoc, 4, (255,00,00))

############ Showing images #############

    cv.imshow('source image', img)

    k = cv.waitKey(0)

    return maxLoc


# scan4laser("realDot.jpg")
