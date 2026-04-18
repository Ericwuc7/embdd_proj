# Run on Raspberry Pi 3B+ (Clone and Run)

## 1) Clone
```bash
git clone https://github.com/Ericwuc7/embdd_proj.git
cd embdd_proj/embdd_complete_project
```

## 2) Hardware Connections
Follow: `docs/HARDWARE_CONNECTIONS.md`

Quick summary:
- PIR: VCC->5V, GND->GND, OUT->D8 (Arduino)
- Buzzer: +->D9, -->GND
- LED: anode->D10 via 220Ω, cathode->GND
- Arduino USB -> Raspberry Pi USB
- USB camera -> Raspberry Pi USB

## 3) Arduino Upload
Upload `arduino/pir_with_alarm.ino` to Arduino Uno using Arduino IDE.

## 4) Raspberry Pi Setup
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-opencv
cd raspberry_pi
pip3 install -r requirements.txt
```

## 5) Configure Environment
```bash
cp .env.example .env
nano .env
```
Set:
- `SERIAL_PORT` (usually `/dev/ttyACM0`)
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `CAMERA_INDEX` (usually `0`)

## 6) Run Components
### Serial-only test
```bash
python3 phase2_serial_reader.py
```

### Full system (serial + camera + Telegram + dashboard)
```bash
python3 phase4_complete_system.py
```
Dashboard: `http://<raspberry-pi-ip>:5000`

## 7) Optional AI Model
Place model at:
- `raspberry_pi/ai_models/human_detector.pt`

If no model is loaded, the system uses OpenCV HOG person detection fallback.

## 8) Troubleshooting
See `docs/TROUBLESHOOTING.md`
