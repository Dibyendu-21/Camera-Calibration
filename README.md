# Camera Calibration
This repo shows how to calibrate camera and undistort any image taken by that camera. The object used is a Chessboard since Checkerboard patterns are distinct and easy to detect in an image. Further the corners of squares on the checkerboard are ideal for localizing them because they have sharp gradients in two directions. 

The goal of the calibration process is to find the 3×3 matrix K which contains information specfic to the camera namely, focal length ( fx,fy), optical centers ( cx,cy) , the 3×3 rotation matrix and the 3×1 translation vector using a set of known 3D points and their corresponding image coordinates which finally can undistort an image taken by that camera. 

In summary, a camera calibration algorithm has the following inputs and outputs

    Input: Collection of 20 images from different view points whose 2D image and 3D world coordinates are known.
    Intermediate Output: 3×3 camera intrinsic matrix, distortion cofficients, rotation matrix and translation vector.
    Final Output: Undistorted Image using the intermediate results.
    
## Design Pipeline
The Design pipeline is as follows:
* Define real world 3D coordinates of checkerboard.
* Locate the chessboard corners in image (Image Points).
* Calibrate the camera and get the distortion cofficients, camera matrix, translation and rotaional matrix
* Read the distorted image.
* Find the optimal camera matrix and ROI based on alpha free scaling parameter.
* Undistort the image.
* Extract and display only that portion of undisroted image which contains all valid pixels using the ROI found earlier.
   
