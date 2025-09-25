# Computer Vision Lab

This project contains step-by-step learning materials for computer vision using OpenCV.

## Setup

1. **Clone or download this project**

2. **Create virtual environment** (recommended):

   ```bash
   python3 -m venv .venv
   ```

3. **Activate virtual environment**:

   ```bash
   # macOS/Linux
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
computer vision/
├── .venv/                 # Virtual environment
├── lesson-2-io/          # Lesson 2: Basic Input/Output
│   ├── io_image.py       # Read/write images
│   ├── io_video.py       # Play video files
│   ├── io_webcam.py      # Access webcam
│   ├── data/             # Sample images & videos
│   └── README.md         # Lesson 2 documentation
├── requirements.txt      # Python dependencies
├── pyproject.toml       # Modern Python project config
└── README.md            # Main documentation
```

## Lessons

### Lesson 2: Input/Output (IO)

Learn the basics of reading images, videos, and webcam with OpenCV.

📁 **Folder:** `lesson-2-io/`

**What you'll learn:**

- Reading and saving images
- Playing video files
- Real-time webcam access

**How to run:**

```bash
cd "lesson-2-io"
python io_image.py    # Image demo
python io_video.py    # Video demo
python io_webcam.py   # Webcam demo (press 'q' to exit)
```

## Dependencies

- OpenCV (opencv-python) - Computer vision library
