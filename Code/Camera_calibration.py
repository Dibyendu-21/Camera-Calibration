# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:59:30 2021

@author: Sonu
"""
import numpy as np
import cv2 as cv
import glob

#Setting the termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

#Preparing the object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((13*12,3), np.float32)
objp[:,:2] = np.mgrid[0:13,0:12].T.reshape(-1,2)

#Arrays to store object points and image points from all the images
objpoints = [] #3d point in real world space
imgpoints = [] #2d points in image plane
images = glob.glob('Sample_Images/*.tif')

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #Finding the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (13,12), None)
    #If corners are found, add object points, image points after refining them
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        #Drawing and displaying the corners
        cv.drawChessboardCorners(img, (13,12), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(1000)

cv.destroyAllWindows()

#Calibrating the camera and getting the distortion cofficient, camera matrix, translation and rotaional matrix
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

print("Camera matrix : \n")
print(mtx)
print("dist : \n")
print(dist)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)

#Reading the distorted image
img = cv.imread('Sample_Images/Image11.tif')
h,  w = img.shape[:2]

#Finding the optimal camera matrix based on alpha free scaling parameter
#It also returns ROI which is bounded rectangle spawning across valid pixels
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

#Undistorting the image
dst = cv.undistort(img, mtx, dist, None, newcameramtx)

#Keeping and displaying only that portion of image which contains all valid pixels
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult_opencv.png', dst)