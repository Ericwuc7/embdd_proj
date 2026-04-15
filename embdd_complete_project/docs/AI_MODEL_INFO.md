# AI Model Info

The project supports two detection paths:

1. **Custom model path (optional):**
   - Put model at `raspberry_pi/ai_models/human_detector.pt`
   - Extend `ai_models/model_loader.py` for your model runtime

2. **Fallback detector (default):**
   - OpenCV HOG person detector
   - Works out-of-the-box after OpenCV install

Use fallback first, then integrate your `.pt` model for better accuracy.
