# Profile Picture Human Verification System

This system verifies whether a profile picture contains a human face, helping maintain professional standards on social media platforms.

## Features

- Detects human faces in profile pictures
- Provides clear verification results
- Easy to integrate into existing systems
- Professional and reliable face detection

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script:

```bash
python human_verification.py
```

2. When prompted, enter the path to the profile picture you want to verify.

3. The system will analyze the image and provide:
   - Verification status (Approved/Rejected)
   - Detailed message about the detection results

## How It Works

The system uses OpenCV's Haar Cascade Classifier to detect human faces in images. It:

1. Loads the image
2. Converts it to grayscale
3. Applies face detection algorithms
4. Returns verification results based on the presence of human faces

## Requirements

- Python 3.7 or higher
- OpenCV
- NumPy

## Note

This system is designed to detect the presence of human faces, not to verify the identity of the person in the image. It's meant to be used as a basic verification tool to ensure profile pictures contain human faces.
