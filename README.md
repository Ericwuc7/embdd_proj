# AI Room Intruder Detection System with Telegram Notifications

## Introduction
This project aims to create an AI room intruder detection system that sends notifications via Telegram when unexpected intrusions are detected.

## Phase 1: Arduino Code
In this phase, we will set up the Arduino to detect movement and send data to a Python script through the serial interface.

### Arduino Code
```cpp
#include <Servo.h>

Servo servo;
int sensorPin = 2; // Motion sensor connected to digital pin 2

void setup() {
  Serial.begin(9600);
  pinMode(sensorPin, INPUT);
  servo.attach(9); // Servo connected to digital pin 9
}

void loop() {
  int state = digitalRead(sensorPin);
  if (state == HIGH) {
    Serial.println("Intruder Detected!");
    servo.write(90); // Move servo
  } else {
    servo.write(0); // Reset servo
  }
  delay(1000);
}
```  

## Phase 2: Python Serial Reader
This phase will use Python to read data from the Arduino.

### Python Serial Reader Code
```python
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)  # Update the port as necessary

def main():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)  # Process the data here

if __name__ == '__main__':
    time.sleep(2)  # Wait for the Arduino to reset
    main()
```  

## Phase 3: Camera + AI Detection
In this phase, we'll integrate a camera with AI capabilities to detect intrusions using pre-trained models.

### Requirements
- OpenCV
- TensorFlow / Keras

### Sample Code
```python
import cv2

# Load your pre-trained AI model here

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    if detect_intruder(frame):  # Implement your detection logic
        print("Intruder Detected!")
        # Trigger Telegram notification
    cv2.imshow('Camera Feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
```  

## Phase 4: Complete System with Telegram Bot
This phase includes integrating the Python script with Telegram API for notifications.

### Code to Send Notifications
```python
import requests

TELEGRAM_API_URL = 'https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage'
CHAT_ID = '<YOUR_CHAT_ID>'

def send_alert(message):
    payload = {'chat_id': CHAT_ID, 'text': message}
    requests.post(TELEGRAM_API_URL, data=payload)

# Example usage
send_alert('Intruder detected!')
```  

## Hardware Connections
- Motion Sensor to Arduino Pin 2
- Servo Motor to Pin 9
- Camera connected via USB

## Installation Guide
1. Connect the hardware components as shown above.
2. Upload the Arduino code to the Arduino board.
3. Install the necessary Python libraries: `pip install pyserial opencv-python requests`
4. Configure the Python scripts with the correct device paths and Telegram bot credentials.
5. Run the Python scripts to start monitoring.

## Folder Structure
```
embdd_proj/
├── .gitkeep
├── arduino_code/
│   ├── .gitkeep
│   └── arduino_code.ino
├── python_code/
│   ├── .gitkeep
│   ├── serial_reader.py
│   ├── ai_detection.py
│   └── telegram_notifications.py
└── README.md
```

## Conclusion
This comprehensive guide provides the necessary steps and code to set up an AI room intruder detection system with Telegram notifications.