# Virtual Mouse

[![Virtual Mouse Banner](https://via.placeholder.com/1200x300?text=Virtual+Mouse)](https://github.com/yourusername/virtual-mouse)

A Python-based virtual mouse that lets you control your computer's cursor using hand gestures captured via your webcam. This project leverages advanced computer vision and gesture recognition techniques to offer a touchless, intuitive interface.

## Overview

Virtual Mouse uses [Mediapipe](https://google.github.io/mediapipe/), [OpenCV](https://opencv.org/), and [PyAutoGUI](https://pyautogui.readthedocs.io/) for real-time hand tracking and mouse control. The system detects hand landmarks, interprets gestures, and translates them into mouse actions.

### How It Works

```mermaid
flowchart TD
    A[Webcam Input] --> B[Mediapipe Hand Tracking]
    B --> C{Gesture Detection}
    C -->|Index & Thumb Gesture| D[Left Click / Double Click]
    C -->|Middle & Thumb Gesture| E[Right Click]
    C -->|Fingers Aligned| F[Scrolling]
    D & E & F --> G[PyAutoGUI Interface]
    G --> H[OS Mouse Control]

Features
Real-Time Hand Tracking: Uses Mediapipe to accurately detect and track hand landmarks.
Gesture-Based Actions:
Left Click & Double Click: Triggered by pinching the index finger and thumb.
Right Click: Triggered by pinching the middle finger and thumb.
Scrolling: Activated when fingers are aligned horizontally and moved vertically.
Smooth Cursor Movement: Implements a smoothing algorithm for fluid and responsive cursor control.
Customizable Parameters: Easily modify thresholds and sensitivity settings in the code.
Architecture
The project is organized into four main modules:

Input Module: Captures live video feed from the webcam.
Processing Module: Converts video frames, detects hand landmarks, and processes gestures.
Gesture Recognition Module: Analyzes hand positions to decide the corresponding mouse action.
Output Module: Uses PyAutoGUI to send commands to the operating system for mouse control.
mermaid
Copy
Edit
graph LR
    A[Webcam Capture] --> B[Frame Preprocessing]
    B --> C[Hand Landmark Detection]
    C --> D[Gesture Analysis]
    D --> E[Mouse Action Mapping]
    E --> F[OS Control via PyAutoGUI]

Requirements
Python 3.x
OpenCV
Mediapipe
PyAutoGUI
NumPy
Installation
Clone the Repository:

git clone https://github.com/yourusername/virtual-mouse.git
cd virtual-mouse
Set Up a Virtual Environment (Optional but Recommended):

python -m venv venv
source venv/bin/activate   # For Windows use: venv\Scripts\activate
Install Dependencies:

pip install opencv-python mediapipe pyautogui numpy
Usage
Ensure Your Webcam is Connected: Make sure your computer’s webcam is working.

Run the Script:

python Virtual\ Mouse.py
Control the Mouse:
Left Click / Double Click: Pinch your index finger and thumb together.
Right Click: Pinch your middle finger and thumb together.
Scrolling: Align your fingers (index, middle, ring, and pinky) horizontally and move them vertically.
Exit the Application: Press q in the display window to quit.

Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
Mediapipe: For providing advanced hand tracking.
OpenCV: For essential computer vision capabilities.
PyAutoGUI: For simplifying mouse automation.
