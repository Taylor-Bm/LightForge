# Multi-Scale Feature Extraction for Artifact Reduction in Low-Light Imaging

## Project Overview

This repository implements a robust multi-scale feature extraction pipeline for reducing artifacts and enhancing image quality in low-light photography and medical imaging.

## Objectives

1. Develop a multi-scale feature extraction method that reduces noise and artifacts in low-light images.
2. Evaluate performance using PSNR, SSIM, and visual comparisons.
3. Compare the proposed method against baseline approaches such as CLAHE and gamma correction.

## Methodology

- Multi-scale Gaussian and Laplacian pyramid decomposition.
- Per-scale denoising and adaptive detail enhancement.
- Fusion with tone mapping and contrast equalization.
- Benchmarking across image pairs with ground truth.

## Repository structure

- `src/`
  - `multiscale_artifact_reduction.py`: core enhancement algorithm and CLI.
  - `benchmark.py`: dataset evaluation and benchmark comparison.
  - `utils.py`: image utilities, metric computation, and helpers.
- `tests/`: unit tests for the pipeline.
- `matlab/`: MATLAB prototype stub for future algorithm development.
- `requirements.txt`: Python dependencies.

## Getting started

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the enhancement demo:

```bash
python -m src.multiscale_artifact_reduction --input path/to/low_light.jpg --output path/to/enhanced.png
```

3. Run a dataset benchmark:

```bash
python -m src.benchmark --input_dir datasets/LOL/low --gt_dir datasets/LOL/gt --output_dir results/LOL
```

4. Run unit tests:

```bash
python -m unittest discover -s tests
```

## Dataset recommendation

- LOL (Low-Light dataset)
- SID (See-in-the-Dark)
- Dark Face

For benchmarking, use paired low-light and reference images.

## Notes

- The algorithm is designed to be extensible for future deep learning models.
- Baseline comparisons include CLAHE, gamma correction, and edge-preserving filtering.
- Use the benchmark script to generate CSV metrics and save enhanced outputs.
