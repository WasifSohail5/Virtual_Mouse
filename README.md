# Virtual Mouse with Hand Gestures 🚀

Welcome to **Virtual Mouse with Hand Gestures** – an innovative, touch-free system that transforms your hand movements into seamless mouse control! This project leverages the power of **MediaPipe** for real-time hand tracking, **OpenCV** for video processing, and **PyAutoGUI** for controlling your computer’s mouse. Enjoy a futuristic way to interact with your computer without any physical device!

---

## 🌟 Project Overview

Imagine controlling your computer simply by moving your hand in front of a webcam. This project provides:

- **Smooth Pointer Movement:**  
  The mouse pointer follows your index finger with adjustable smoothing to ensure responsive yet stable movement.
  
- **Click Gestures:**  
  - **Left Click:** Performed by pinching your thumb and index finger together.  
  - **Right Click:** Performed by pinching your thumb and middle finger together.  
  - **Double Left Click:** Two consecutive left-click gestures within a specified time trigger a double click.

- **Scroll Functionality:**  
  When you align the bases of your four fingers (landmarks 5, 9, 13, and 17) and move them vertically:
  - **Scroll Up:** Hand moving upward scrolls up.
  - **Scroll Down:** Hand moving downward scrolls down.
  - The scroll sensitivity has been enhanced for a faster response.

- **Customizable Sensitivity and Gestures:**  
  Fine-tune pointer sensitivity, click thresholds, and scroll responsiveness to perfectly match your style.

---

## 🔍 Key Features

- **Real-Time Hand Tracking:**  
  Utilizes MediaPipe to detect 21 hand landmarks for precise gesture recognition.
  
- **Dynamic Gesture Recognition:**  
  - **Smooth Pointer Control:** With adjustable smoothing for natural movement.
  - **Multi-Click Gestures:** Supports left, right, and double left click actions.
  - **High-Sensitivity Scrolling:** Activated by aligning specific finger base landmarks and moving vertically.

- **Interactive Debug Interface:**  
  A resizable window displays live video feed, gesture debug info, and real-time feedback on actions.

- **User-Friendly & Adaptable:**  
  Simple to set up and configure, making it easy to integrate into various applications or extend with additional gestures.

---

## 📝 How It Works

1. **Initialization:**  
   The system initializes the webcam, MediaPipe hand tracking module, and prepares the GUI window.

2. **Frame Processing:**  
   - Captures a frame from the webcam.
   - Flips the frame for a mirror-like experience.
   - Processes the frame using MediaPipe to detect hand landmarks.

3. **Gesture Detection:**  
   - **Pointer Movement:**  
     Maps the position of your index finger (with smoothing) to your screen coordinates.
   - **Click Gestures:**  
     - **Left Click:** Triggered when the distance between thumb and index finger is below a set threshold.
     - **Right Click:** Triggered when the distance between thumb and middle finger is below the threshold.
     - **Double Left Click:** Two left-click gestures within a 0.5-second window trigger a double click.
   - **Scroll Mode:**  
     When the bases of your index, middle, ring, and pinky fingers (landmarks 5, 9, 13, and 17) are aligned (low x-axis variation), the system switches to scroll mode. Vertical movement of these points scrolls the page up or down with high sensitivity.

4. **Output & Feedback:**  
   The processed frame with annotated landmarks and debug info is displayed. The system continuously updates the pointer position and detects gestures in real-time.

---

## 🔄 Flow Diagram

```mermaid
flowchart TD
    A[Start Program] --> B[Initialize Webcam & Modules]
    B --> C[Capture & Flip Frame]
    C --> D[Process Frame with MediaPipe]
    D --> E{Hand Landmarks Detected?}
    E -- Yes --> F[Draw Landmarks on Frame]
    F --> G[Extract Key Landmarks]
    G --> H[Determine Gesture Mode]
    H -- Scroll Mode --> I[Compute Average Y of Finger Bases]
    I --> J[Calculate Vertical Difference]
    J --> K[Execute Scroll (Up/Down)]
    H -- Normal Mode --> L[Map Index Finger to Screen Coordinates]
    L --> M[Apply Smoothing Filter]
    M --> N[Move Mouse Pointer]
    N --> O[Detect Click Gestures]
    O -- Thumb-Index Pinch --> P[Left Click / Double Left Click]
    O -- Thumb-Middle Pinch --> Q[Right Click]
    P & Q --> R[Update Debug Info on Frame]
    R --> S[Display Frame]
    S --> T{Window Closed or 'q' pressed?}
    T -- Yes --> U[Release Resources & Exit]
    T -- No --> C
💻 Installation
Clone the Repository:

git clone https://github.com/yourusername/virtual-mouse.git
cd virtual-mouse
Install Dependencies:

Ensure you have Python 3.x installed, then run:

pip install opencv-python mediapipe pyautogui numpy
Run the Project:

python virtual_mouse.py
🕹️ How to Use
Pointer Movement:
Move your hand in front of the webcam; your index finger controls the pointer with smooth, responsive motion.

Click Gestures:

Left Click: Pinch your thumb and index finger together.
Right Click: Pinch your thumb and middle finger together.
Double Left Click: Perform two left-click pinches within 0.5 seconds.
Scroll Functionality:

Activate Scroll Mode:
Align the bases of your index, middle, ring, and pinky fingers (landmarks 5, 9, 13, 17) so that they are nearly in a vertical line.
Scroll:
Move your hand vertically:
Upward movement: Scrolls up.
Downward movement: Scrolls down.
The scroll sensitivity is set high for quick and efficient scrolling.
🎨 Customization
Pointer Sensitivity:
Adjust the smoothing factor to make the mouse pointer more or less responsive.

Click Settings:
Modify CLICK_THRESHOLD and click_cooldown to fine-tune pinch gesture detection.

Scroll Settings:
Tweak threshold_x_std, scroll_threshold, and scroll_factor to optimize scrolling speed and sensitivity.

🤝 Contributing
Contributions are welcome! If you have ideas, bug fixes, or improvements, please feel free to:

Fork the repository.
Create a new branch for your feature or fix.
Submit a pull request with detailed descriptions of your changes.
📞 Connect with Me
For questions, feedback, or professional networking, please connect with me on LinkedIn.

📜 License
This project is licensed under the MIT License.

Enjoy exploring this futuristic way to control your computer, and happy coding! 🚀







