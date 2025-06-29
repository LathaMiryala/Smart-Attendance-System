# 👁️ Smart Attendance System using Blink Detection

This Python-based project uses **MediaPipe** and **OpenCV** to implement a smart attendance system. The system detects a user's **face and eye activity** through a webcam. If the user's eyes remain closed for **2 or more seconds**, the system assumes a blink (or intentional closure) and captures an image of their face, saving it to the desktop.

---

## 📌 Features

* Face detection using **MediaPipe**
* Eye detection using **OpenCV Haar Cascade**
* Automatically captures an image when eyes are closed for 2+ seconds
* Saves the snapshot with a **timestamped filename** in an `images` folder on the desktop

---

## 🛠️ Requirements

Install the required libraries before running the script:

```bash
pip install opencv-python mediapipe
```

---

## 🚀 How It Works

1. Starts the webcam stream.
2. Detects the **face** using MediaPipe.
3. Detects **eyes** using Haar Cascades.
4. If eyes are **not detected** for 2+ seconds:

   * Takes a snapshot of the face.
   * Saves it as `face_YYYY-MM-DD_HH-MM-SS.jpg` in the desktop's `images` folder.
5. Displays the webcam feed with bounding boxes.
6. Automatically exits after saving a snapshot or when the user presses **'q'**.

---

## 📁 Output

Images will be saved in:

```
Desktop/images/
```

Example filename:

```
face_2025-06-29_10-30-00.jpg
```

---

## 📸 Demo

![demo](https://github.com/your-username/your-repo-name/assets/demo-placeholder.gif)

*Replace this with your own GIF/screenshot*

---

## 🧠 Built With

* [OpenCV](https://opencv.org/)
* [MediaPipe](https://google.github.io/mediapipe/)
* Python 3.7+

---

## 📌 Usage

To run the script:

```bash
python your_script_name.py
```

Make sure your webcam is accessible and you're in a well-lit environment for better detection accuracy.

---

