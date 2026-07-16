# TINE Model Interface Documentation

## Overview

The TINE Model Interface provides a unified, efficient framework for training, validating, and testing image enhancement models. It streamlines the workflow from hyperparameter optimization to production deployment.

## Features

✅ **Hyperparameter Optimization** - Automated grid search with validation metrics  
✅ **Batch Processing** - Efficient processing of multiple images  
✅ **Baseline Comparisons** - Compare against CLAHE, gamma correction, and edge-preserving filters  
✅ **Comprehensive Metrics** - PSNR, SSIM, and statistical analysis  
✅ **Configuration Management** - Save/load configurations for reproducibility  
✅ **CLI Interface** - Easy command-line access to all features  
✅ **Performance Testing** - Speed and memory efficiency benchmarks  

---

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Optional: Install psutil for performance testing
pip install psutil
```

---

## Quick Start

### 1. Train with Hyperparameter Search

```bash
python -m src.model_cli train \
  --input_dir data/low_light \
  --gt_dir data/ground_truth \
  --output_dir training_logs
```

### 2. Validate on Test Set

```bash
python -m src.model_cli validate \
  --input_dir data/test_low \
  --gt_dir data/test_gt \
  --output_dir validation_results
```

### 3. Test Single Image

```bash
python -m src.model_cli test-single \
  --image path/to/image.jpg \
  --output result.png
```

### 4. Test Batch with Baselines

```bash
python -m src.model_cli test-batch \
  --input_dir data/test \
  --output_dir test_results \
  --compare_baselines
```

---

## Python API

### Basic Usage

```python
from src.model_interface import ModelInterface, ModelConfig

# Create interface with default config
model = ModelInterface()

# Or with custom config
config = ModelConfig(
    levels=4,
    detail_strength=0.8,
    gamma=0.75,
    clahe_clip=2.0,
    use_dl=True
)
model = ModelInterface(config)
```

### Training

```python
# Hyperparameter search
results = model.train(
    input_dir="data/low_light",
    gt_dir="data/ground_truth",
    param_grid={
        "levels": [2, 3, 4, 5],
        "detail_strength": [0.5, 0.8, 1.0],
        "gamma": [0.6, 0.75, 0.9],
        "clahe_clip": [1.5, 2.0, 2.5],
    },
    n_samples=10
)

print(f"Best parameters: {results['best_params']}")
print(f"Results file: {results['results_file']}")
```

### Validation

```python
# Validate on test set
stats = model.validate(
    input_dir="data/test_low",
    gt_dir="data/test_gt",
    output_dir="validation_results",
    save_images=True
)

print(f"PSNR: {stats['psnr']['mean']:.2f} ± {stats['psnr']['std']:.2f} dB")
print(f"SSIM: {stats['ssim']['mean']:.4f} ± {stats['ssim']['std']:.4f}")
```

### Testing

```python
# Test single image
enhanced = model.test_single(
    image_path="path/to/image.jpg",
    output_path="result.png"
)

# Test batch
summary = model.test(
    input_dir="data/test",
    output_dir="test_results",
    compare_baselines=True
)

print(f"Successful: {summary['successful']}/{summary['total_images']}")
```

### Configuration Management

```python
# Get current config
config = model.get_config()
print(config)

# Update config
model.update_config(
    levels=5,
    detail_strength=1.0,
    gamma=0.8
)

# Save config
model.save_config("my_config.json")

# Load config
from src.model_interface import ModelConfig
loaded_config = ModelConfig.from_dict(json.load(open("my_config.json")))
model = ModelInterface(loaded_config)
```

---

## API Reference

### ModelConfig

Configuration container for model parameters.

**Parameters:**
- `levels` (int): Number of pyramid levels (default: 4)
- `denoise_strength` (int): Denoising strength for NLM (default: 10)
- `detail_strength` (float): Detail enhancement strength (default: 0.8)
- `gamma` (float): Gamma correction factor (default: 0.75)
- `clahe_clip` (float): CLAHE contrast limit (default: 2.0)
- `use_dl` (bool): Use deep learning denoising (default: True)
- `device` (str): Compute device - "cuda" or "cpu" (default: auto-detect)

**Methods:**
- `to_dict()` - Convert to dictionary
- `from_dict(config_dict)` - Create from dictionary

### ModelTrainer

Handles model training and hyperparameter optimization.

**Methods:**
- `train_hyperparameters(input_dir, gt_dir, param_grid, n_samples)` - Grid search optimization
- `save_config(path)` - Save configuration to JSON

### ModelValidator

Validates model performance on test datasets.

**Methods:**
- `validate(input_dir, gt_dir, output_dir, save_images)` - Validate on image pairs

**Returns:**
```python
{
    "total_images": int,
    "psnr": {
        "mean": float,
        "std": float,
        "min": float,
        "max": float
    },
    "ssim": {
        "mean": float,
        "std": float,
        "min": float,
        "max": float
    },
    "metrics": [
        {"image": str, "psnr": float, "ssim": float},
        ...
    ]
}
```

### ModelTester

Tests model on individual images and batches.

**Methods:**
- `test_single(image_path, output_path)` - Process single image
- `test_batch(input_dir, output_dir, compare_baselines)` - Process batch

### ModelInterface

Unified interface combining all components.

**Methods:**
- `train(input_dir, gt_dir, param_grid, n_samples)` - Run training
- `validate(input_dir, gt_dir, output_dir, save_images)` - Run validation
- `test(input_dir, output_dir, compare_baselines)` - Run batch testing
- `test_single(image_path, output_path)` - Test single image
- `update_config(**kwargs)` - Update configuration
- `get_config()` - Get current configuration
- `save_config(path)` - Save configuration

---

## Command-Line Interface

### Train Command

```bash
python -m src.model_cli train \
  --input_dir <path> \
  --gt_dir <path> \
  [--output_dir <path>] \
  [--n_samples <int>]
```

**Options:**
- `--input_dir` (required): Directory with low-light images
- `--gt_dir` (required): Directory with ground truth images
- `--output_dir`: Output directory (default: training_logs)
- `--n_samples`: Samples per parameter combination (default: 10)

### Validate Command

```bash
python -m src.model_cli validate \
  --input_dir <path> \
  --gt_dir <path> \
  [--output_dir <path>] \
  [--levels <int>] \
  [--detail_strength <float>] \
  [--gamma <float>] \
  [--clahe_clip <float>]
```

### Test-Single Command

```bash
python -m src.model_cli test-single \
  --image <path> \
  [--output <path>] \
  [--levels <int>] \
  [--detail_strength <float>] \
  [--gamma <float>] \
  [--clahe_clip <float>]
```

### Test-Batch Command

```bash
python -m src.model_cli test-batch \
  --input_dir <path> \
  [--output_dir <path>] \
  [--compare_baselines] \
  [--levels <int>] \
  [--detail_strength <float>] \
  [--gamma <float>] \
  [--clahe_clip <float>]
```

### Config Command

```bash
python -m src.model_cli config \
  [--show] \
  [--save <path>] \
  [--load <path>] \
  [--levels <int>] \
  [--detail_strength <float>] \
  [--gamma <float>] \
  [--clahe_clip <float>]
```

### Benchmark Command

```bash
python -m src.model_cli benchmark \
  --input_dir <path> \
  --gt_dir <path> \
  [--output_dir <path>]
```

---

## Testing

Run the comprehensive test suite:

```bash
# Run all tests
python -m src.test_model_interface

# Run specific test class
python -m unittest src.test_model_interface.TestModelInterface

# Run with verbose output
python -m unittest src.test_model_interface -v
```

**Test Coverage:**
- Configuration management
- Training and hyperparameter search
- Validation on image pairs
- Single and batch testing
- Full workflow integration
- Performance benchmarks

---

## Workflow Examples

### Example 1: Complete Pipeline

```python
from src.model_interface import ModelInterface, ModelConfig

# Initialize
model = ModelInterface()

# Step 1: Train with hyperparameter search
print("Training...")
train_results = model.train(
    input_dir="data/train_low",
    gt_dir="data/train_gt",
    n_samples=20
)

# Step 2: Apply best parameters
best_params = train_results["best_params"]
model.update_config(
    levels=best_params["levels"],
    detail_strength=best_params["detail_strength"],
    gamma=best_params["gamma"],
    clahe_clip=best_params["clahe_clip"]
)

# Step 3: Validate
print("Validating...")
val_stats = model.validate(
    input_dir="data/val_low",
    gt_dir="data/val_gt"
)

# Step 4: Test on new data
print("Testing...")
test_summary = model.test(
    input_dir="data/test",
    compare_baselines=True
)

# Step 5: Save configuration
model.save_config("best_config.json")
```

### Example 2: Quick Testing

```python
from src.model_interface import ModelInterface

model = ModelInterface()

# Test single image
enhanced = model.test_single(
    "path/to/low_light.jpg",
    "path/to/output.png"
)

# Test batch
summary = model.test("data/test_images")
print(f"Processed {summary['successful']} images successfully")
```

### Example 3: Custom Configuration

```python
from src.model_interface import ModelInterface, ModelConfig

# Create custom config
config = ModelConfig(
    levels=5,
    detail_strength=1.2,
    gamma=0.8,
    clahe_clip=2.5,
    use_dl=True
)

model = ModelInterface(config)

# Validate with custom settings
stats = model.validate(
    input_dir="data/test_low",
    gt_dir="data/test_gt"
)

print(f"PSNR: {stats['psnr']['mean']:.2f} dB")
print(f"SSIM: {stats['ssim']['mean']:.4f}")
```

---

## Output Files

### Training Output
- `training_logs/hyperparameter_search.json` - Search results with all parameter combinations
- `training_logs/config_*.json` - Saved configurations

### Validation Output
- `validation_results/validation_results.json` - Detailed metrics
- `validation_results/*.png` - Enhanced images (if save_images=True)

### Testing Output
- `test_results/test_summary.json` - Test summary
- `test_results/*_proposed.png` - Proposed method results
- `test_results/*_clahe.png` - CLAHE baseline
- `test_results/*_gamma.png` - Gamma correction baseline
- `test_results/*_edge.png` - Edge-preserving baseline

---

## Performance Tips

1. **Use GPU**: Set `device="cuda"` for faster processing
2. **Batch Processing**: Process multiple images at once for efficiency
3. **Reduce Pyramid Levels**: Lower `levels` for faster processing
4. **Disable Deep Learning**: Set `use_dl=False` for CPU-only systems
5. **Sample Subset**: Use `n_samples` parameter to speed up training

---

## Troubleshooting

### Out of Memory
- Reduce image size
- Disable deep learning (`use_dl=False`)
- Reduce pyramid levels
- Process fewer images at once

### Slow Processing
- Use GPU acceleration
- Reduce pyramid levels
- Disable baseline comparisons
- Use smaller images

### No Images Found
- Check directory paths
- Ensure images are .png or .jpg format
- Verify file permissions

---

## License

Educational/Research Use

---

## Support

For issues or questions, refer to the main README.md or check the test suite for usage examples.
