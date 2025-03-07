import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()


CLICK_THRESHOLD = 40
click_cooldown = 1.0
last_click_time = 0

double_click_threshold = 0.5
last_left_click_time = 0

smoothing = 0.5
prev_x, prev_y = None, None

threshold_x_std = 20
scroll_threshold = 5
scroll_factor = 10
prev_avg_y = None

cv2.namedWindow("Virtual Mouse", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Virtual Mouse", 1000, 800)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror view.
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    scroll_mode = False

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb = hand_landmarks.landmark[4]
            index_finger = hand_landmarks.landmark[8]
            middle_finger = hand_landmarks.landmark[12]

            index_base = hand_landmarks.landmark[5]
            middle_base = hand_landmarks.landmark[9]
            ring_base = hand_landmarks.landmark[13]
            pinky_base = hand_landmarks.landmark[17]

            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)
            index_x, index_y = int(index_finger.x * w), int(index_finger.y * h)
            middle_x, middle_y = int(middle_finger.x * w), int(middle_finger.y * h)

            index_base_x, index_base_y = int(index_base.x * w), int(index_base.y * h)
            middle_base_x, middle_base_y = int(middle_base.x * w), int(middle_base.y * h)
            ring_base_x, ring_base_y = int(ring_base.x * w), int(ring_base.y * h)
            pinky_base_x, pinky_base_y = int(pinky_base.x * w), int(pinky_base.y * h)

            dist_index_thumb = math.hypot(index_x - thumb_x, index_y - thumb_y)
            dist_middle_thumb = math.hypot(middle_x - thumb_x, middle_y - thumb_y)

            debug_text = f'Idx-Thmb: {int(dist_index_thumb)} | Mid-Thmb: {int(dist_middle_thumb)}'
            cv2.putText(frame, debug_text, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            # Scroll mode detection using landmarks 5,9,13,17.
            fingers_x = np.array([index_base_x, middle_base_x, ring_base_x, pinky_base_x])
            if np.std(fingers_x) < threshold_x_std:
                scroll_mode = True
                avg_y = np.mean([index_base_y, middle_base_y, ring_base_y, pinky_base_y])
                if prev_avg_y is not None:
                    diff = avg_y - prev_avg_y
                    if abs(diff) > scroll_threshold:
                        pyautogui.scroll(-int(diff * scroll_factor))
                        cv2.putText(frame, "Scrolling", (index_x, index_y - 40),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
                prev_avg_y = avg_y
            else:
                scroll_mode = False
                prev_avg_y = None

            current_time = time.time()
            
            # Scrollwheel
            if not scroll_mode:
                screen_x = np.interp(index_x, [0, w], [0, screen_width])
                screen_y = np.interp(index_y, [0, h], [0, screen_height])
                if prev_x is None:
                    prev_x, prev_y = screen_x, screen_y
                else:
                    smoothed_x = prev_x + smoothing * (screen_x - prev_x)
                    smoothed_y = prev_y + smoothing * (screen_y - prev_y)
                    screen_x, screen_y = smoothed_x, smoothed_y
                    prev_x, prev_y = screen_x, screen_y

                pyautogui.moveTo(screen_x, screen_y, duration=0.01)

                # Left Click
                if dist_index_thumb < CLICK_THRESHOLD and (current_time - last_click_time) > click_cooldown:
                    # Check if two left clicks occur within the double click threshold.
                    if (current_time - last_left_click_time) < double_click_threshold:
                        pyautogui.doubleClick()
                        cv2.putText(frame, "Double Left Click!", (index_x, index_y - 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        last_left_click_time = 0  # Reset
                    else:
                        pyautogui.click()
                        cv2.putText(frame, "Left Click!", (index_x, index_y - 20),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        last_left_click_time = current_time
                    last_click_time = current_time

                # Right Click
                elif dist_middle_thumb < CLICK_THRESHOLD and (current_time - last_click_time) > click_cooldown:
                    pyautogui.rightClick()
                    last_click_time = current_time
                    cv2.putText(frame, "Right Click!", (middle_x, middle_y - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.getWindowProperty("Virtual Mouse", cv2.WND_PROP_VISIBLE) < 1:
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
