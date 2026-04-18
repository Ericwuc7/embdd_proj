# Raspberry Pi Runtime

## Files
- `config.py`: environment config loader
- `phase2_serial_reader.py`: serial-only monitor
- `telegram_notifier.py`: Telegram API notifier
- `phase4_complete_system.py`: complete monitoring pipeline
- `web_dashboard.py`: Flask dashboard app
- `ai_models/model_loader.py`: detector loader (fallback included)

## Setup
```bash
pip3 install -r requirements.txt
cp .env.example .env
```
