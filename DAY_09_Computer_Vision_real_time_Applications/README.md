# DAY 9 - Computer Vision Real Time Applications

## Overview
Day 9 focused on advanced Computer Vision applications using OpenCV and Deep Learning techniques.

The session covered:
- Video processing
- Image alignment
- Panorama creation
- HDR imaging
- Object tracking
- Deep Learning based object detection
- Pose detection

All implementations were performed using Google Colab.

---

# Topics Covered

## 5. Writing a Video using OpenCV

### Topics Learned
- Reading video from source
- Reading and displaying one frame
- Displaying video files
- Writing video using OpenCV
- Reading frames and saving output video

### Learning Outcome
- Understanding video processing using OpenCV
- Working with frames
- Saving processed video output

## Google Colab Link
https://colab.research.google.com/drive/1kP2GYpm1O7L3cOF3rhnhS-DKl_rDJ8p4?usp=sharing

---

# 6. Image Alignment

Image alignment is used to match and transform images into the same coordinate system.

## Steps Covered

### Step 1
Read template image and scanned image

### Step 2
Find keypoints in both images

### Step 3
Match keypoints between images

### Step 4
Find Homography matrix

### Step 5
Warp image for alignment

### Learning Outcome
- Understanding feature matching
- Image registration concepts
- Perspective transformation using homography

## Google Colab Link
https://colab.research.google.com/drive/1t8tWlahK-HcD66Hd7Wb-nLtqKNRSqS2L?usp=sharing

---

# 7. Panorama Creation using OpenCV

Panorama stitching combines multiple images into one wide-angle image.

## Steps Covered
- Find keypoints in all images
- Find pairwise correspondences
- Estimate pairwise homographies
- Refine homographies
- Stitch images with blending

### Learning Outcome
- Understanding image stitching
- Feature detection and matching
- Panorama generation techniques

## Google Colab Link
https://colab.research.google.com/drive/17n9xz6VgGb856L2qLX4y7uQYBjIpl-yk?usp=sharing

---

# 8. High Dynamic Range (HDR) Imaging

HDR imaging combines multiple exposure images to improve dynamic range.

## Basic Concepts
- Standard images are limited to 8-bit range (0–255)
- Bright pixels saturate
- Dark pixels lose detail

## Steps Covered

### Step 1
Capture multiple exposure images

### Step 2
Align images

### Step 3
Estimate camera response function

### Step 4
Merge exposures into HDR image

### Step 5
Apply tone mapping

### Learning Outcome
- Understanding exposure blending
- HDR image generation
- Tone mapping techniques

## Google Colab Link
https://colab.research.google.com/drive/1NbMLfMRU2LLPIcpCYUc8M2KqcPiK0Dfk?usp=sharing

---

# 9. Object Tracking in Videos

Object tracking identifies and follows objects frame by frame in videos.

## Tracker Algorithms Explored

| Tracker | Description |
|---------|-------------|
| BOOSTING | Traditional boosting tracker |
| MIL | Multiple Instance Learning |
| KCF | Kernelized Correlation Filters |
| CSRT | Accurate tracking method |
| TLD | Recovers from occlusions |
| MEDIANFLOW | Good for slow predictable motion |
| GOTURN | Deep Learning based tracker |
| MOSSE | Fastest tracker |

---

## GOTURN Tracker Workflow

### Steps Covered
- Create tracker instance
- Read input video
- Setup output video
- Define bounding box
- Initialize tracker
- Read frames and track object

### Learning Outcome
- Real-time object tracking
- Understanding tracking algorithms
- Deep learning based tracking

## Google Colab Link
https://colab.research.google.com/drive/1B8lwFsll-z9hUqvDFUV42cabw60rOyA-?usp=sharing

---

# 10. Deep Learning Based Object Detection

Object detection identifies and classifies objects in images.

## Topics Covered
- Checking class labels
- Reading TensorFlow model
- Detecting objects
- Displaying detected objects
- Viewing results
- Understanding false alarms

### Learning Outcome
- Understanding object detection pipelines
- Working with TensorFlow models
- Bounding box visualization

## Google Colab Link
https://colab.research.google.com/drive/1Hs3r1qQJ_r2Lmv4k47S2uh0hi-EyA6dN?usp=sharing

---

# 11. Pose Detection

Realtime multi-person 2D pose estimation using Part Affinity Fields.

## Topics Covered
- Loading Caffe model
- Reading image
- Converting image to blob
- Running inference (forward pass)
- Extracting body points
- Displaying skeleton and keypoints

### Learning Outcome
- Human pose estimation
- Skeleton detection
- Deep learning inference workflow

## Google Colab Link
https://colab.research.google.com/drive/1B-1SFTUbGxNn1vXgHS79Gh3HH2XPTapF?usp=sharing

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming |
| OpenCV | Computer Vision |
| TensorFlow | Deep Learning |
| Caffe Model | Pose Detection |
| Google Colab | Cloud execution environment |

---

# Concepts Learned

- Video processing
- Image transformation
- Feature matching
- Panorama stitching
- HDR imaging
- Real-time object tracking
- Deep learning object detection
- Human pose estimation

---

# Learning Outcome

By completing Day 9, learned:
- Advanced OpenCV operations
- Video manipulation techniques
- Real-time computer vision applications
- Deep learning integration in vision tasks
- Object detection and tracking
- Pose estimation techniques

---

# Author
Ibrahim