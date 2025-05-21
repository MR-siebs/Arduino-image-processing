import cv2 as cv
import numpy as np



# IK HEB HIER ZOVEEL TIJD IN VERSPILD :'(


def getMiddle(imgDil, img):
    contours,hierarchy = cv.findContours(imgDil,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(f"Contour Area: {area}")
        if area > 100:
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)

            x, y, w, h = cv.boundingRect(approx)

            middlePoint = np.average(cnt, axis=0)
            middlePoint = (int(middlePoint[0][0]),int(middlePoint[0][1]))
            print(middlePoint)

            cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            cv.circle(img, middlePoint, 4, (255,0,255), cv.FILLED)
            return(middlePoint)



def scan4laser(srcPath):

############ Retreiving base images #############

    src = cv.imread(srcPath)    # retreives source image

    img = cv.resize(src, (int(src.shape[1]/3), int(src.shape[0]/3)))

    # isolates the blue and green channel to identify the red dot
    imgBG = img.copy()

    imgBG[:,:,2] = 0
    imgGray = cv.cvtColor(imgBG, cv.COLOR_RGB2GRAY)

    # isolates the red channel for shadow correction
    imgRed = img.copy()

    imgRed[:,:,0] = 0   
    imgRed[:,:,1] = 0
    imgRed = cv.cvtColor(imgRed, cv.COLOR_RGB2GRAY)


    kernel = np.ones((2,2),np.uint8)    # the kernel is required for image dilation
    

############ Image processing #############
    
    imgBlur = cv.GaussianBlur(imgGray, (7,7), 1 )
    imgCanny = cv.Canny(imgBlur, 50, 50)
    imgDil = cv.dilate(imgCanny, kernel, iterations=1)

    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(imgGray)
    

    laserPoint = getMiddle(imgDil, img)

    cv.circle(img, maxLoc, 2, (00,255,00), cv.FILLED)
    cv.circle(img, maxLoc, 5, (00,255,00), 2)
    

############ Showing images #############

    cv.imshow('source image', img)
    cv.imshow('Red channel', imgRed)
    cv.imshow('Grayscale image', imgGray)
    cv.imshow('Canny image', imgCanny)
    cv.imshow('Dilated image', imgDil)
    k = cv.waitKey(0)


scan4laser("realDot.jpg")
