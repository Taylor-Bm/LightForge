# TINE Model Interface - Simple Startup Guide

## 🚀 Quick Start (Choose One Method)

### Method 1: Interactive Menu (EASIEST)
```bash
python interactive_menu.py
```
This opens a friendly menu where you can select commands by number.

### Method 2: Direct Python
```bash
python run_model.py --help
python run_model.py train --help
python run_model.py validate --help
```

### Method 3: Python Module
```bash
python -m src.model_cli --help
python -m src.model_cli train --help
python -m src.model_cli validate --help
```

### Method 4: Batch File (Simple)
```bash
model_interface.bat help
model_interface.bat train --input_dir data\low --gt_dir data\gt
```

---

## 📋 Common Commands

### Show Help
```bash
python interactive_menu.py
```
Or:
```bash
python run_model.py --help
```

### Test Single Image
```bash
python run_model.py test-single --image test.jpg --output result.png
```

### Train Model
```bash
python run_model.py train --input_dir data\low --gt_dir data\gt
```

### Validate Model
```bash
python run_model.py validate --input_dir data\test_low --gt_dir data\test_gt
```

### Test Batch
```bash
python run_model.py test-batch --input_dir data\test
```

### Show Configuration
```bash
python run_model.py config --show
```

### Run Tests
```bash
python -m src.test_model_interface
```

---

## ✅ Installation Check

### 1. Check Python
```bash
python --version
```
Should show Python 3.9+

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Test Interactive Menu
```bash
python interactive_menu.py
```
Should show menu with 10 options

### 4. Test Direct Python
```bash
python run_model.py --help
```
Should show help message

---

## 🎯 Recommended Workflow

### Step 1: Open Interactive Menu
```bash
python interactive_menu.py
```

### Step 2: Select Option
- Press `1` for Training
- Press `2` for Validation
- Press `3` for Single Image Test
- etc.

### Step 3: Follow Prompts
- Enter directory paths when asked
- Wait for processing to complete
- Results will be saved to output directory

### Step 4: Check Results
- Training: `training_logs/hyperparameter_search.json`
- Validation: `validation_results/validation_results.json`
- Testing: `test_results/test_summary.json`

---

## 💡 Tips

1. **Use Interactive Menu for Easiest Experience**
   ```bash
   python interactive_menu.py
   ```

2. **Use Direct Python for Scripting**
   ```bash
   python run_model.py train --input_dir data\low --gt_dir data\gt
   ```

3. **Use Batch File for Quick Commands**
   ```bash
   model_interface.bat test-single --image test.jpg --output result.png
   ```

4. **Always Run from TINE Directory**
   ```bash
   cd C:\Users\LENOVO\Desktop\TINE
   ```

---

## 🔧 Troubleshooting

### Issue: "No module named 'src'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Python not found"
**Solution:**
1. Install Python 3.9+
2. Add to PATH
3. Restart terminal

### Issue: "Permission denied"
**Solution:**
1. Run Command Prompt as Administrator
2. Navigate to TINE directory
3. Run command again

---

## 📚 Documentation

- `INDEX.md` - Navigation guide
- `QUICK_START.md` - Quick start
- `MODEL_INTERFACE_GUIDE.md` - Complete reference
- `TROUBLESHOOTING.md` - Troubleshooting

---

## 🎉 Ready to Go!

Choose your preferred method and start using TINE Model Interface:

1. **Easiest:** `python interactive_menu.py`
2. **Direct:** `python run_model.py train --input_dir data\low --gt_dir data\gt`
3. **Batch:** `model_interface.bat help`

**Happy enhancing! 🚀**
