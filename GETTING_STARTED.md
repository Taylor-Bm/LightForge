# TINE Model Interface - Getting Started

## ⚠️ IMPORTANT: Install Dependencies First!

### Step 1: Run Setup
Double-click or run:
```bash
setup.bat
```

This will install all required dependencies.

### Step 2: Wait for Installation
The installation may take 2-5 minutes. Do NOT close the window.

### Step 3: Verify Installation
After setup completes, run:
```bash
model_interface.bat help
```

---

## 🚀 After Installation

### Option 1: Interactive Menu (EASIEST)
```bash
python interactive_menu.py
```
A friendly menu will appear with 10 options to choose from.

### Option 2: Batch File
```bash
model_interface.bat help
model_interface.bat test-single --image test.jpg --output result.png
model_interface.bat train --input_dir data\low --gt_dir data\gt
```

### Option 3: Direct Python
```bash
python -m src.model_cli --help
python -m src.model_cli train --input_dir data\low --gt_dir data\gt
```

---

## 📋 Quick Commands

### Show Help
```bash
model_interface.bat help
```

### Test Single Image
```bash
model_interface.bat test-single --image test.jpg --output result.png
```

### Train Model
```bash
model_interface.bat train --input_dir data\low --gt_dir data\gt
```

### Validate Model
```bash
model_interface.bat validate --input_dir data\test_low --gt_dir data\test_gt
```

### Test Batch
```bash
model_interface.bat test-batch --input_dir data\test
```

### Show Configuration
```bash
model_interface.bat config --show
```

### Run Tests
```bash
model_interface.bat test
```

---

## ✅ Installation Checklist

- [ ] Run `setup.bat`
- [ ] Wait for installation to complete
- [ ] Run `model_interface.bat help`
- [ ] See help menu displayed
- [ ] Try `python interactive_menu.py`
- [ ] See interactive menu with 10 options

---

## 🎯 Recommended First Steps

1. **Install Dependencies**
   ```bash
   setup.bat
   ```

2. **Open Interactive Menu**
   ```bash
   python interactive_menu.py
   ```

3. **Select Option 5: Show Configuration**
   - Press `5` and Enter
   - See current settings

4. **Try Option 3: Test Single Image**
   - Press `3` and Enter
   - Enter path to test image
   - See enhanced result

---

## 📚 Documentation

After installation, read:
- `STARTUP_GUIDE.md` - Simple startup guide
- `QUICK_START.md` - Quick start guide
- `MODEL_INTERFACE_GUIDE.md` - Complete reference
- `INDEX.md` - Navigation guide

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Run `setup.bat` again

### Issue: "Python not found"
**Solution:** 
1. Install Python 3.9+ from https://www.python.org/
2. Check "Add Python to PATH" during installation
3. Restart terminal

### Issue: Setup takes too long
**Solution:** This is normal. Wait 2-5 minutes for all packages to install.

### Issue: Permission denied
**Solution:**
1. Right-click `setup.bat`
2. Select "Run as administrator"

---

## 🎉 Success!

If you can run `model_interface.bat help` without errors, everything is working!

**Next:** Try `python interactive_menu.py` for an easy-to-use interface.

---

**Happy enhancing! 🚀**
