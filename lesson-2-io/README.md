# Lesson 2: Input/Output (IO) with OpenCV

This lesson covers the basics of input and output with OpenCV, including reading/writing images, videos, and accessing webcam.

## Files

- `io_image.py` - Read, write, and display images
- `io_video.py` - Play video files
- `io_webcam.py` - Access webcam (press 'q' to exit)
- `data/` - Folder containing sample images and videos

## How to Run

Make sure you have activated the virtual environment and installed dependencies:

```bash
# Activate virtual environment (from root folder)
source ../.venv/bin/activate

# Install dependencies (if not already done)
pip install -r ../requirements.txt
```

Then run the scripts:

```bash
# Run image script
python io_image.py

# Run video script
python io_video.py

# Run webcam script
python io_webcam.py
```

## What You'll Learn

### 1. Reading and Writing Images (`io_image.py`)
- `cv2.imread()` - Read image from file
- `cv2.imwrite()` - Save image to file
- `cv2.imshow()` - Display image in window
- `cv2.waitKey()` - Wait for keyboard input

### 2. Reading Video (`io_video.py`)
- `cv2.VideoCapture()` - Open video file
- `video.read()` - Read frame from video
- Loop to play all frames
- `video.release()` - Release video resource

### 3. Accessing Webcam (`io_webcam.py`)
- `cv2.VideoCapture(0)` - Access webcam (device 0)
- Real-time video capture
- `cv2.destroyAllWindows()` - Close all OpenCV windows

## Tips

- Press 'q' to exit from webcam
- Make sure webcam is not being used by other applications
- Supported image formats: JPG, PNG, BMP, etc.
- Supported video formats: MP4, AVI, MOV, etc.