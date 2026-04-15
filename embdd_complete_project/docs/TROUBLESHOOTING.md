# Troubleshooting

## Serial port not found
- Check `ls /dev/ttyACM* /dev/ttyUSB*`
- Update `SERIAL_PORT` in `.env`
- Ensure Arduino is connected and firmware is uploaded

## Camera not opening
- Verify camera index (`CAMERA_INDEX`) in `.env`
- Test: `python3 -c "import cv2; c=cv2.VideoCapture(0); print(c.isOpened())"`

## Telegram not sending
- Verify `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`
- Make sure Raspberry Pi has internet access

## Dashboard not reachable
- Ensure script is running
- Open `http://<pi-ip>:5000`
- If needed, allow port 5000 in firewall/router
