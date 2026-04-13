# Project Overview

This project is designed for detecting human movement and sending alerts via a Telegram bot.

## Quick Start
1. Clone the repository.
2. Follow the instructions in the `arduino` and `raspberry_pi` directories for setup.
3. Train the model as described in the `training` directory.

## Project Structure
```
embdd_proj/
├── arduino/
│   ├── README.md
│   ├── pir_motion_detection.ino
│   └── pir_with_alarm.ino
├── docs/
│   ├── HARDWARE_CONNECTIONS.md
│   ├── TROUBLESHOOTING.md
│   ├── AI_MODEL_INFO.md
│   ├── TELEGRAM_SETUP.md
│   ├── CAMERA_SETUP.md
│   └── REMOTE_DASHBOARD.md
├── raspberry_pi/
│   ├── README.md
│   ├── requirements.txt
│   ├── config.py
│   ├── phase2_serial_reader.py
│   ├── telegram_notifier.py
│   ├── ai_models/
│   │   └── model_loader.py
│   ├── phase4_complete_system.py
│   ├── web_dashboard.py
│   └── templates/
│       └── dashboard.html
├── training/
│   ├── README.md
│   └── train_human_detector.py
└── LEARNING_ROADMAP.md
```
