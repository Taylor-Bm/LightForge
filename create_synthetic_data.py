import cv2
import numpy as np
import os
from pathlib import Path
from tqdm import tqdm

def create_synthetic_pair(index, base_path_low, base_path_gt):
    # Create a random "medical-like" image (circular shapes, gradients)
    size = (512, 512)
    gt = np.zeros(size, dtype=np.uint8)
    
    # Add random blobs (simulating anatomy)
    for _ in range(5):
        center = (np.random.randint(100, 412), np.random.randint(100, 412))
        axes = (np.random.randint(50, 150), np.random.randint(50, 150))
        angle = np.random.randint(0, 360)
        color = np.random.randint(100, 255)
        cv2.ellipse(gt, center, axes, angle, 0, 360, color, -1)
    
    # Add some "noise" textures
    noise = np.random.normal(0, 5, size).astype(np.uint8)
    gt = cv2.add(gt, noise)
    
    # Create "Low Light" version
    # 1. Reduce intensity (simulate low exposure)
    low = (gt.astype(np.float32) * 0.15).astype(np.uint8)
    
    # 2. Add significant Gaussian noise
    gauss = np.random.normal(20, 15, size).astype(np.uint8)
    low = cv2.add(low, gauss)
    
    # Save images
    cv2.imwrite(str(base_path_gt / f"sample_{index:03d}.png"), gt)
    cv2.imwrite(str(base_path_low / f"sample_{index:03d}.png"), low)

def main():
    print("Generating 90 synthetic image pairs for LightForge...")
    
    data_dir = Path("data")
    low_dir = data_dir / "low"
    gt_dir = data_dir / "gt"
    
    low_dir.mkdir(parents=True, exist_ok=True)
    gt_dir.mkdir(parents=True, exist_ok=True)
    
    for i in tqdm(range(90)):
        create_synthetic_pair(i, low_dir, gt_dir)
    
    print(f"\nSuccess! Generated 90 pairs in {data_dir}")
    print(f"Low-light images: {low_dir}")
    print(f"Ground truth images: {gt_dir}")

if __name__ == "__main__":
    main()
