from __future__ import annotations

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Starter training launcher for human detector")
    parser.add_argument("--dataset", required=True, help="Path to training dataset")
    parser.add_argument("--epochs", type=int, default=50, help="Training epochs")
    parser.add_argument("--output", default="human_detector.pt", help="Output model file name")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    print("Training placeholder")
    print(f"Dataset: {args.dataset}")
    print(f"Epochs: {args.epochs}")
    print(f"Output: {args.output}")
    print("Integrate your preferred framework (YOLO/PyTorch) here.")


if __name__ == "__main__":
    main()
