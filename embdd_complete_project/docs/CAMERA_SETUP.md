# Camera Setup

1. Connect USB camera to Raspberry Pi.
2. Test camera:

```bash
python3 -c "import cv2; c=cv2.VideoCapture(0); print('opened:', c.isOpened())"
```

3. If false, try index 1 or 2 in `.env` with `CAMERA_INDEX`.
