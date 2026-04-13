# AI Room Intruder Detection System (Raspberry Pi 3B+ + Arduino Uno)

This repo provides a complete, step-by-step embedded + AI project to detect human intruders in a room using:
- Arduino Uno + PIR sensor (motion trigger)
- Raspberry Pi 3B+ + USB camera + AI model (.pt)
- Telegram notifications
- Web dashboard for live camera viewing

## Quick Start (Pi 3B+)
1) Clone:
   git clone https://github.com/Ericwuc7/embdd_proj.git
   cd embdd_proj/raspberry_pi
2) Install dependencies:
   pip3 install -r requirements.txt
3) Place your trained model:
   Copy your .pt into raspberry_pi/ai_models/human_detector.pt
4) Configure:
   Edit raspberry_pi/config.py and set BOT_TOKEN + CHAT_ID
5) Run full system:
   python3 phase4_complete_system.py
6) (Optional) Start dashboard:
   python3 web_dashboard.py

## Where to start
- Read LEARNING_ROADMAP.md
- Follow PROJECT_SETUP.md

## Project Tree
See the folder structure in this README and the individual README files under arduino/ and raspberry_pi/.
