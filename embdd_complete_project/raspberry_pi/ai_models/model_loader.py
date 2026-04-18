from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import cv2

BoundingBox = Tuple[int, int, int, int]


@dataclass
class DetectionResult:
    humans: List[BoundingBox]


class HumanDetector:
    """Fallback human detector using OpenCV HOG descriptor."""

    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = Path(model_path) if model_path else None
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def detect(self, frame) -> DetectionResult:
        rects, _weights = self.hog.detectMultiScale(
            frame,
            winStride=(8, 8),
            padding=(8, 8),
            scale=1.05,
        )
        boxes: List[BoundingBox] = []
        for x, y, w, h in rects:
            boxes.append((int(x), int(y), int(w), int(h)))
        return DetectionResult(humans=boxes)
