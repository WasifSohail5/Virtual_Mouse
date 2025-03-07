# Virtual Mouse with Hand Gestures 🚀

Welcome to **Virtual Mouse with Hand Gestures** – a cutting-edge, touch-free system that empowers you to control your computer’s mouse using intuitive hand movements captured by your webcam. This project harnesses state-of-the-art libraries to deliver a futuristic user experience!

---

## 🌟 Project Overview

Imagine interacting with your computer without any physical device—simply use your hand! This project provides:

- **Smooth Pointer Movement:**  
  Your index finger drives the mouse pointer with customizable smoothing for responsive yet stable control.
  
- **Click Gestures:**  
  - **Left Click:** Pinch your thumb and index finger together.
  - **Right Click:** Pinch your thumb and middle finger together.
  - **Double Left Click:** Two rapid left-click gestures (pinches) trigger a double click.

- **Scroll Functionality:**  
  Align the bases of your four fingers (landmarks 5, 9, 13, and 17) and move them vertically:
  - **Scroll Up:** Hand moving upward scrolls up.
  - **Scroll Down:** Hand moving downward scrolls down.
  - Enhanced scroll sensitivity ensures quick and efficient scrolling.

- **Customizable Gestures & Sensitivity:**  
  Fine-tune pointer sensitivity, click thresholds, and scroll responsiveness to suit your personal style.

---

## 🛠️ Libraries and Models Used

The project is built with several powerful libraries and models. Below is a quick reference:

| Library/Tool  | Description                                                       | Version (Recommended) |
|---------------|-------------------------------------------------------------------|-----------------------|
| **OpenCV**    | Real-time computer vision library for video capture and processing | 4.x                   |
| **MediaPipe** | Real-time hand tracking and landmark detection model               | 0.x                   |
| **PyAutoGUI** | Cross-platform GUI automation for mouse control                    | 0.x                   |
| **NumPy**     | Library for numerical computations and array processing            | 1.x                   |

---

## 💻 Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/virtual-mouse.git
   cd virtual-mouse
Install Dependencies:

Ensure you have Python 3.x installed, then run:

pip install opencv-python mediapipe pyautogui numpy
Run the Project:

python virtual_mouse.py
🕹️ How to Use
Pointer Movement:
Simply move your hand in front of the webcam; your index finger controls the pointer with smooth and responsive motion.

Click Gestures:

Left Click: Pinch your thumb and index finger together.
Right Click: Pinch your thumb and middle finger together.
Double Left Click: Execute two rapid left-click gestures (within 0.5 seconds) to trigger a double click.
Scroll Functionality:

Activate Scroll Mode:
Align the bases of your index, middle, ring, and pinky fingers (landmarks 5, 9, 13, and 17) so they form a near vertical line.
Scroll:
Move your hand vertically:
Upward movement: Scrolls up.
Downward movement: Scrolls down.
The scroll sensitivity is optimized for quick and efficient scrolling.
🎨 Customization
Pointer Sensitivity:
Adjust the smoothing factor in the code to modify how responsive the mouse pointer is.

Click Settings:
Tweak CLICK_THRESHOLD and click_cooldown to fine-tune how pinch gestures trigger click actions.

Scroll Settings:
Modify threshold_x_std, scroll_threshold, and scroll_factor to optimize scroll speed and responsiveness.

🤝 Contributing
Contributions are welcome! If you have ideas, bug fixes, or improvements, please:

Fork the repository.
Create a new branch for your feature or fix.
Submit a pull request with detailed descriptions of your changes.
📞 Connect with Me
For questions, feedback, or professional networking, please connect with me on LinkedIn.

📜 License
This project is licensed under the MIT License.
