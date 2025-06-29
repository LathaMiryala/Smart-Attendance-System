import cv2
import mediapipe as mp
import os
import time
from datetime import datetime

# 1. Create 'images' folder on Desktop if it doesn't exist
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
save_dir = os.path.join(desktop_path, "images")
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 2. Initialize MediaPipe Face Detection
mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(min_detection_confidence=0.6)

# 3. Initialize OpenCV Haar Cascade for Eye Detection
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 4. Start Webcam
cap = cv2.VideoCapture(0)
snapshot_taken = False
image_path = ""
closed_eyes_start_time = None  # Timer for continuous closed eyes

while True:
    success, frame = cap.read()
    if not success:
        break

    # Convert to RGB for Mediapipe
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(img_rgb)

    if results.detections and not snapshot_taken:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x = int(bbox.xmin * iw)
            y = int(bbox.ymin * ih)
            w = int(bbox.width * iw)
            h = int(bbox.height * ih)

            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Crop the face region for eye detection
            face_region = frame[y:y + h, x:x + w]

            # Convert to grayscale for eye detection
            gray = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)

            # Detect eyes
            eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(eyes) == 0:
                if closed_eyes_start_time is None:
                    closed_eyes_start_time = time.time()  # Start timer
                else:
                    elapsed = time.time() - closed_eyes_start_time
                    if elapsed >= 2 and not snapshot_taken:  # Eyes closed for 2 seconds
                        face_img = frame[y:y+h, x:x+w]
                        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                        filename = f"face_{timestamp}.jpg"
                        image_path = os.path.join(save_dir, filename)
                        cv2.imwrite(image_path, face_img)
                        print(f"[✓] Blink detected! Snapshot saved at: {image_path}")
                        snapshot_taken = True
                        break
            else:
                closed_eyes_start_time = None  # Reset timer if eyes open

    cv2.imshow("Blink Detection - Face Capture", frame)

    if snapshot_taken or cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
