# Learning Roadmap

## Phase 1: Hardware Basics
- Wire PIR, buzzer, and LED to Arduino.
- Validate PIR signal events over serial.

## Phase 2: Raspberry Pi Serial Integration
- Read motion events from Arduino with `phase2_serial_reader.py`.

## Phase 3: Vision + Human Detection
- Connect camera and validate stream.
- Add model-based or fallback person detection.

## Phase 4: Full Alert System
- Combine PIR + vision.
- Send Telegram alerts and monitor web dashboard.
