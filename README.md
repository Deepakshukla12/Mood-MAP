# 🎭 MoodMap - Emotion Detection & Recognition System

## 🌟 Overview
The *MoodMap* is an advanced *Emotion Detection & Recognition System* that leverages deep learning and computer vision to analyze human emotions in real-time. It recognizes facial expressions and speech patterns to enhance user interaction and mental well-being. Future versions aim to integrate IoT for seamless smart applications.

## 🚀 Features
✅ *Real-time Facial Emotion Recognition* - Detects emotions from live webcam feed using OpenCV and deep learning.
✅ *Speech Emotion Detection* 🎙 - (Coming Soon) Analyzes vocal tones for emotion classification.
✅ *Web-based Interface* 🌐 - Interactive UI powered by Flask.
✅ *Live Video Feed Processing* 📹 - Streams video with real-time emotion overlays.
✅ *Emotion Logging* 📊 - Stores emotions with timestamps for analysis.
✅ *Future IoT Integration* 🤖 - Smart applications like mood-based lighting!

---

## 🛠 Technology Stack
| Technology | Purpose |
|------------|---------|
| Flask | Backend Web Framework |
| OpenCV | Face Detection |
| Keras + TensorFlow | Deep Learning Model |
| HTML, CSS, JS | Frontend Development |
| SQLite/JSON | Data Storage |
| Haar Cascade Classifier | Face Detection |
| NumPy & Pandas | Data Processing |

---

## 📥 Installation
### 🔧 Prerequisites
Ensure you have *Python 3.7+* installed.

### 📌 Setup Steps
1. *Clone the Repository* 📂
   bash
   git clone (https://github.com/Coderkingkrishna/Emotion-detection)
   cd moodmap
   
2. *Create a Virtual Environment* 🌍
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. *Install Dependencies* ⚙
   bash
   pip install -r requirements.txt
   
4. *Download & Place the Pre-trained Model* 🤖
   Ensure emotiondetector.json and emotiondetector.h5 are in the project root.
5. *Run the Application* 🚀
   bash
   python realtime.py
   
   Access the interface at:
   
   http://127.0.0.1:5000/
   

---

## 🎯 Usage Guide
📌 *Start Analysis:* Click on "Start Analyzing" on the home page.
📌 *Live Results:* View real-time emotion detection.
📌 *Access Logs:* Visit /emotion_results for past detections.

---

## 📂 File Structure

moodmap/
├── static/

│   ├── styles.css  (UI Styling)
│   ├── images/  (Assets & Backgrounds)
├── templates/
│   ├── index.html  (Home Page)
│   ├── face_analysis.html  (Emotion Detection Page)
│   ├── signup.html  (Sign Up Page)
├── emotiondetector.json  (Model Structure)
├── emotiondetector.h5  (Model Weights)
├── realtime.py  (Main Flask App)
├── requirements.txt  (Dependencies)
├── README.md  (This file)



---

## 🔮 Future Enhancements
🎤 *Speech Emotion Recognition* - Voice-based analysis integration.
🔗 *IoT Connectivity* - Smart devices triggering responses based on detected emotions.
📊 *Advanced Analytics* - Trend-based emotional insights.
📱 *Mobile App Version* - Track emotions on-the-go.

---

## 👥 Contributors
- Deepak Shukla 🎓
- Krishna Agrawal 🎓
  
## 📜 License
Licensed under *MIT License* - see the LICENSE file for details.

🌟 Stay tuned for updates and improvements! 🚀
