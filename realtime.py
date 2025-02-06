from flask import Flask, render_template, Response, jsonify
import cv2
from keras.models import model_from_json
import numpy as np
import time
from datetime import datetime

app = Flask(__name__)

# Load the emotion detection model
json_file = open("emotiondetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)
model.load_weights("emotiondetector.h5")

# Load Haar Cascade for face detection
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

# Define labels for emotions
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

# List to store results with timestamp
emotion_results = []

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

def generate_frames():
    webcam = cv2.VideoCapture(0)
    last_capture_time = time.time()
    
    while True:
        success, frame = webcam.read()
        if not success:
            break
        else:
            current_time = time.time()
            # Run emotion detection every 5 seconds
            if current_time - last_capture_time >= 1:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face = gray[y:y + h, x:x + w]
                    face = cv2.resize(face, (48, 48))
                    face = extract_features(face)
                    
                    # Predict emotion
                    prediction = model.predict(face)
                    emotion_label = labels[prediction.argmax()]
                    
                    # Add the detected emotion and timestamp to results
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    emotion_results.append({"emotion": emotion_label, "timestamp": timestamp})
                    
                    # Draw rectangle around face and put the emotion label
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                last_capture_time = current_time
            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/face_analysis')
def face_analysis():
    return render_template('face_analysis.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route to fetch emotion results as JSON
@app.route('/emotion_results')
def get_emotion_results():
    return jsonify(emotion_results)

if __name__ == "__main__":
    app.run(debug=True)
