# 🎨 TINE Model Interface - Complete Training & Testing Suite

A production-ready, unified interface for training, validating, and testing the TINE image enhancement system. Provides automated hyperparameter optimization, comprehensive validation, and flexible testing workflows.

## ✨ Features

- **🚀 Automated Training** - Grid search hyperparameter optimization
- **📊 Comprehensive Validation** - PSNR/SSIM metrics with statistical analysis
- **🧪 Flexible Testing** - Single image, batch processing, baseline comparisons
- **⚙️ Configuration Management** - Save/load configurations for reproducibility
- **🖥️ Multiple Interfaces** - Python API, CLI, and Windows batch scripts
- **📚 Extensive Documentation** - Quick start, complete guide, and examples
- **✅ Robust Testing** - 20+ unit and integration tests
- **⚡ Performance Optimized** - GPU support, efficient batch processing

## 📦 What's Included

### Core Components
- `src/model_interface.py` - Unified model interface (500+ lines)
- `src/model_cli.py` - Command-line interface (400+ lines)
- `src/test_model_interface.py` - Comprehensive test suite (600+ lines)

### Documentation
- `QUICK_START.md` - 5-minute quick start guide
- `MODEL_INTERFACE_GUIDE.md` - Complete API reference and examples
- `IMPLEMENTATION_SUMMARY.md` - Architecture and design overview

### Automation
- `model_interface.bat` - Windows batch script for easy execution

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Test Single Image
```bash
python -m src.model_cli test-single --image test.jpg --output result.png
```

### 3. Train with Hyperparameter Search
```bash
python -m src.model_cli train --input_dir data/low --gt_dir data/gt
```

### 4. Validate Results
```bash
python -m src.model_cli validate --input_dir data/test_low --gt_dir data/test_gt
```

## 📖 Usage Examples

### Python API

```python
from src.model_interface import ModelInterface, ModelConfig

# Quick enhancement
model = ModelInterface()
enhanced = model.test_single("image.jpg", "result.png")

# Full optimization workflow
results = model.train("data/train_low", "data/train_gt")
best_params = results["best_params"]
model.update_config(**best_params)
stats = model.validate("data/test_low", "data/test_gt")
print(f"PSNR: {stats['psnr']['mean']:.2f} dB")
```

### Command-Line Interface

```bash
# Train
python -m src.model_cli train --input_dir data/low --gt_dir data/gt

# Validate
python -m src.model_cli validate --input_dir data/test_low --gt_dir data/test_gt

# Test batch
python -m src.model_cli test-batch --input_dir data/test --compare_baselines

# Manage config
python -m src.model_cli config --show
python -m src.model_cli config --save best_config.json
```

### Windows Batch Script

```bash
# Train
model_interface.bat train --input_dir data\low --gt_dir data\gt

# Validate
model_interface.bat validate --input_dir data\test_low --gt_dir data\test_gt

# Test
model_interface.bat test-single --image test.jpg --output result.png

# Help
model_interface.bat help
```

## 🎯 Common Workflows

### Workflow 1: Quick Enhancement (5 seconds)
```bash
model_interface.bat test-single --image low_light.jpg --output enhanced.png
```

### Workflow 2: Full Optimization (10-30 minutes)
```bash
# Train
model_interface.bat train --input_dir data\train_low --gt_dir data\train_gt

# Validate
model_interface.bat validate --input_dir data\test_low --gt_dir data\test_gt

# Test
model_interface.bat test-batch --input_dir data\new_images
```

### Workflow 3: Comprehensive Benchmark (20-60 minutes)
```bash
model_interface.bat benchmark --input_dir data\train_low --gt_dir data\train_gt
```

## 📊 API Reference

### ModelInterface

Main unified interface for all operations.

```python
model = ModelInterface(config=None)

# Training
results = model.train(input_dir, gt_dir, param_grid, n_samples)

# Validation
stats = model.validate(input_dir, gt_dir, output_dir, save_images)

# Testing
summary = model.test(input_dir, output_dir, compare_baselines)
enhanced = model.test_single(image_path, output_path)

# Configuration
config = model.get_config()
model.update_config(**kwargs)
model.save_config(path)
```

### ModelConfig

Configuration container for model parameters.

```python
config = ModelConfig(
    levels=4,              # Pyramid levels (1-6)
    denoise_strength=10,   # NLM denoising (0-50)
    detail_strength=0.8,   # Enhancement (0.0-2.0)
    gamma=0.75,            # Brightness (0.1-2.0)
    clahe_clip=2.0,        # Contrast (1.0-5.0)
    use_dl=True,           # Deep learning denoising
    device="cuda"          # "cuda" or "cpu"
)
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# All tests
python -m src.test_model_interface

# Specific test class
python -m unittest src.test_model_interface.TestModelInterface -v

# With verbose output
python -m unittest discover -s src -p "test_*.py" -v
```

**Test Coverage:**
- Configuration management (4 tests)
- Training pipeline (3 tests)
- Validation framework (3 tests)
- Testing suite (3 tests)
- Interface integration (5 tests)
- Performance benchmarks (2 tests)

## 📈 Performance

| Operation | Time | Memory |
|-----------|------|--------|
| Single 512x512 image | 2-5s | 50-100 MB |
| Batch of 100 images | 3-8 min | 500-800 MB |
| Hyperparameter search (16 combos) | 10-20 min | 300-500 MB |

## 📁 Output Files

### Training
- `training_logs/hyperparameter_search.json` - All results
- `training_logs/config_*.json` - Saved configurations

### Validation
- `validation_results/validation_results.json` - Metrics
- `validation_results/*.png` - Enhanced images

### Testing
- `test_results/test_summary.json` - Summary
- `test_results/*_proposed.png` - Proposed method
- `test_results/*_clahe.png` - CLAHE baseline
- `test_results/*_gamma.png` - Gamma baseline
- `test_results/*_edge.png` - Edge baseline

## 🔧 Configuration Guide

### Parameter Tuning

**For Darker Images:**
```python
config = ModelConfig(gamma=0.6, detail_strength=1.0)
```

**For Noisy Images:**
```python
config = ModelConfig(levels=5, detail_strength=0.5)
```

**For Maximum Detail:**
```python
config = ModelConfig(levels=5, detail_strength=1.5, clahe_clip=2.5)
```

**For Speed:**
```python
config = ModelConfig(levels=2, use_dl=False)
```

## 📚 Documentation

- **QUICK_START.md** - 5-minute setup and common workflows
- **MODEL_INTERFACE_GUIDE.md** - Complete API reference and examples
- **IMPLEMENTATION_SUMMARY.md** - Architecture and design overview

## ⚠️ Troubleshooting

### Python not found
Install Python 3.9+ and add to PATH

### No images found
Check directory paths and ensure images are .png or .jpg

### Out of memory
- Reduce image size
- Use fewer pyramid levels
- Process fewer images at once

### Slow processing
- Use GPU (if available)
- Reduce pyramid levels
- Disable baseline comparisons

## 🎓 Learning Path

1. **Beginner:** Read `QUICK_START.md`, run `test-single`
2. **Intermediate:** Read `MODEL_INTERFACE_GUIDE.md`, run training
3. **Advanced:** Study `src/model_interface.py`, customize components

## 🔄 Architecture

```
ModelInterface (Unified Interface)
├── ModelTrainer (Hyperparameter Optimization)
├── ModelValidator (Validation Framework)
└── ModelTester (Testing Suite)
```

## ✅ Quality Assurance

- ✅ Type hints throughout
- ✅ Comprehensive docstrings
- ✅ Error handling and validation
- ✅ 20+ unit and integration tests
- ✅ Performance benchmarks
- ✅ Extensive documentation

## 🚀 Getting Started

```bash
# 1. Install
pip install -r requirements.txt

# 2. Quick test
python -m src.model_cli test-single --image test.jpg --output result.png

# 3. Full training
python -m src.model_cli train --input_dir data/low --gt_dir data/gt

# 4. Run tests
python -m src.test_model_interface
```

## 📊 Metrics Explained

**PSNR (Peak Signal-to-Noise Ratio)**
- Higher is better (typical: 20-40 dB)
- 30+ dB = excellent quality

**SSIM (Structural Similarity Index)**
- Range: 0-1 (higher is better)
- 0.9+ = very similar to ground truth

## 🎉 Key Achievements

✅ Unified interface for all operations  
✅ Automated hyperparameter optimization  
✅ Comprehensive validation framework  
✅ Flexible testing with baselines  
✅ Multiple access methods (API, CLI, batch)  
✅ Extensive documentation  
✅ Robust testing suite  
✅ Production-ready code  

## 📞 Support

- Check `QUICK_START.md` for quick answers
- See `MODEL_INTERFACE_GUIDE.md` for detailed reference
- Review `src/test_model_interface.py` for code examples
- Run `model_interface.bat help` for command help

## 📄 License

Educational/Research Use

---

**Status:** ✅ Complete and Functional  
**Version:** 1.0.0  
**Last Updated:** 2024

**Ready to train, validate, and test efficiently! 🚀**
