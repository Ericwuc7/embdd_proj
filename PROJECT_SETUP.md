# Project Setup (Hardware + Wiring + Steps)

## Required Hardware
- Raspberry Pi 3B+
- Arduino Uno
- PIR motion sensor
- Buzzer + LED + resistor
- USB camera
- Breadboard + jumper wires

## Wiring (Arduino)
**PIR Sensor**
- VCC → 5V
- GND → GND
- OUT → D8

**Buzzer**
- + → D9 (through resistor if passive)
- − → GND

**LED**
- Anode → D10 (through 220Ω resistor)
- Cathode → GND

## USB Connections
- Arduino → Raspberry Pi via USB
- USB Camera → Raspberry Pi USB

## Software Setup (Pi 3B+ OS)
```bash
sudo apt-get update
sudo apt-get install -y python3-pip python3-opencv
cd embdd_proj/raspberry_pi
pip3 install -r requirements.txt
```

## Run Phases
1. **Phase 1:** Upload `arduino/pir_motion_detection.ino` to Arduino
2. **Phase 2:** Run `python3 phase2_serial_reader.py`
3. **Phase 3:** Add your `.pt` model and test camera
4. **Phase 4:** Run `python3 phase4_complete_system.py`

## Where to place your model
`raspberry_pi/ai_models/human_detector.pt`

## Troubleshooting
See `docs/TROUBLESHOOTING.md`