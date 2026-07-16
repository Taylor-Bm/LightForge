# TINE Model Interface - Quick Start Guide

## 🚀 Getting Started in 5 Minutes

### Step 1: Install Dependencies

```bash
cd TINE
pip install -r requirements.txt
```

### Step 2: Prepare Your Data

Create the following directory structure:

```
TINE/
├── data/
│   ├── train_low/          # Low-light training images
│   ├── train_gt/           # Ground truth training images
│   ├── test_low/           # Low-light test images
│   └── test_gt/            # Ground truth test images
```

### Step 3: Run Training

**Option A: Using Batch Script (Windows)**
```bash
model_interface.bat train --input_dir data\train_low --gt_dir data\train_gt
```

**Option B: Using Python CLI**
```bash
python -m src.model_cli train --input_dir data/train_low --gt_dir data/train_gt
```

**Option C: Using Python API**
```python
from src.model_interface import ModelInterface

model = ModelInterface()
results = model.train(
    input_dir="data/train_low",
    gt_dir="data/train_gt"
)
print(f"Best parameters: {results['best_params']}")
```

### Step 4: Validate Results

```bash
# Batch script
model_interface.bat validate --input_dir data\test_low --gt_dir data\test_gt

# Or Python CLI
python -m src.model_cli validate --input_dir data/test_low --gt_dir data/test_gt

# Or Python API
stats = model.validate(
    input_dir="data/test_low",
    gt_dir="data/test_gt"
)
print(f"PSNR: {stats['psnr']['mean']:.2f} dB")
```

### Step 5: Test on New Images

```bash
# Single image
model_interface.bat test-single --image my_image.jpg --output result.png

# Batch with baselines
model_interface.bat test-batch --input_dir data\test --compare_baselines
```

---

## 📊 Common Workflows

### Workflow 1: Quick Test

```bash
# Test single image with default settings
model_interface.bat test-single --image test.jpg --output result.png
```

**Time:** ~5-10 seconds  
**Output:** Enhanced image

---

### Workflow 2: Full Optimization

```bash
# Step 1: Train (find best parameters)
model_interface.bat train --input_dir data\train_low --gt_dir data\train_gt

# Step 2: Validate (measure performance)
model_interface.bat validate --input_dir data\test_low --gt_dir data\test_gt

# Step 3: Test (apply to new data)
model_interface.bat test-batch --input_dir data\new_images
```

**Time:** 5-30 minutes (depending on dataset size)  
**Output:** Optimized parameters, metrics, enhanced images

---

### Workflow 3: Benchmark Comparison

```bash
# Run complete benchmark with all baselines
model_interface.bat benchmark --input_dir data\train_low --gt_dir data\train_gt
```

**Time:** 10-60 minutes  
**Output:** Comparison with CLAHE, gamma correction, edge-preserving filters

---

## 🎯 Parameter Guide

### Key Parameters

| Parameter | Range | Default | Effect |
|-----------|-------|---------|--------|
| `levels` | 1-6 | 4 | Pyramid decomposition depth (higher = more detail) |
| `detail_strength` | 0.0-2.0 | 0.8 | Enhancement intensity (higher = more enhancement) |
| `gamma` | 0.1-2.0 | 0.75 | Brightness correction (lower = brighter) |
| `clahe_clip` | 1.0-5.0 | 2.0 | Contrast enhancement (higher = more contrast) |

### Quick Tuning

**For Darker Images:**
```bash
model_interface.bat validate \
  --input_dir data\test_low \
  --gt_dir data\test_gt \
  --gamma 0.6 \
  --detail_strength 1.0
```

**For Noisy Images:**
```bash
model_interface.bat validate \
  --input_dir data\test_low \
  --gt_dir data\test_gt \
  --levels 5 \
  --detail_strength 0.5
```

**For Maximum Detail:**
```bash
model_interface.bat validate \
  --input_dir data\test_low \
  --gt_dir data\test_gt \
  --levels 5 \
  --detail_strength 1.5 \
  --clahe_clip 2.5
```

---

## 📈 Understanding Results

### Metrics Explained

**PSNR (Peak Signal-to-Noise Ratio)**
- Higher is better (typical range: 20-40 dB)
- Measures overall image quality
- 30+ dB = excellent quality

**SSIM (Structural Similarity Index)**
- Range: 0-1 (higher is better)
- Measures perceptual similarity
- 0.9+ = very similar to ground truth

### Example Output

```
✅ Validation complete!
PSNR: 28.45 ± 2.15 dB
SSIM: 0.8923 ± 0.0145
```

**Interpretation:**
- Average PSNR of 28.45 dB (good quality)
- Consistent results (low std dev)
- High structural similarity to ground truth

---

## 🔧 Configuration Management

### Save Configuration

```bash
model_interface.bat config --save my_config.json
```

### Load Configuration

```bash
model_interface.bat config --load my_config.json
```

### View Current Configuration

```bash
model_interface.bat config --show
```

### Update Parameters

```bash
model_interface.bat config \
  --levels 5 \
  --detail_strength 1.0 \
  --gamma 0.8
```

---

## 🧪 Testing

### Run Full Test Suite

```bash
model_interface.bat test
```

**Tests:**
- Configuration management
- Training pipeline
- Validation metrics
- Single/batch processing
- Performance benchmarks

### Run Specific Tests

```bash
python -m unittest src.test_model_interface.TestModelInterface -v
```

---

## 💡 Tips & Tricks

### 1. Speed Up Processing

```bash
# Use fewer pyramid levels
model_interface.bat validate \
  --input_dir data\test_low \
  --gt_dir data\test_gt \
  --levels 2
```

### 2. Improve Quality

```bash
# Use more pyramid levels and higher detail strength
model_interface.bat validate \
  --input_dir data\test_low \
  --gt_dir data\test_gt \
  --levels 5 \
  --detail_strength 1.2
```

### 3. Batch Processing

```bash
# Process multiple images efficiently
model_interface.bat test-batch \
  --input_dir data\test \
  --output_dir results \
  --compare_baselines
```

### 4. Reproducibility

```bash
# Save configuration for later use
model_interface.bat config --save best_params.json

# Load and use same parameters
model_interface.bat config --load best_params.json
```

---

## ⚠️ Troubleshooting

### Issue: "Python not found"
**Solution:** Install Python 3.9+ and add to PATH

### Issue: "No images found"
**Solution:** Check directory paths and ensure images are .png or .jpg

### Issue: "Out of memory"
**Solution:** 
- Reduce image size
- Use fewer pyramid levels
- Process fewer images at once

### Issue: "Slow processing"
**Solution:**
- Use GPU (if available)
- Reduce pyramid levels
- Disable baseline comparisons

---

## 📚 Next Steps

1. **Read Full Documentation:** See `MODEL_INTERFACE_GUIDE.md`
2. **Explore Examples:** Check `src/test_model_interface.py`
3. **Customize:** Modify parameters for your use case
4. **Deploy:** Use best configuration in production

---

## 🎓 Learning Resources

### Python API Examples

```python
# Example 1: Simple enhancement
from src.model_interface import ModelInterface

model = ModelInterface()
enhanced = model.test_single("image.jpg", "result.png")

# Example 2: Full workflow
results = model.train("data/train_low", "data/train_gt")
best_params = results["best_params"]
model.update_config(**best_params)
stats = model.validate("data/test_low", "data/test_gt")

# Example 3: Custom configuration
from src.model_interface import ModelConfig

config = ModelConfig(
    levels=5,
    detail_strength=1.0,
    gamma=0.8,
    clahe_clip=2.5
)
model = ModelInterface(config)
```

### CLI Examples

```bash
# Train with custom parameters
python -m src.model_cli train \
  --input_dir data/train_low \
  --gt_dir data/train_gt \
  --n_samples 20

# Validate with specific settings
python -m src.model_cli validate \
  --input_dir data/test_low \
  --gt_dir data/test_gt \
  --levels 5 \
  --detail_strength 1.0

# Test batch with baselines
python -m src.model_cli test-batch \
  --input_dir data/test \
  --compare_baselines
```

---

## 📞 Support

For issues or questions:
1. Check `MODEL_INTERFACE_GUIDE.md` for detailed documentation
2. Review test examples in `src/test_model_interface.py`
3. Check error messages and troubleshooting section above

---

**Happy enhancing! 🎉**
