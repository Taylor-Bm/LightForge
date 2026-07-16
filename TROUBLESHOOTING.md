# TINE Model Interface - Troubleshooting Guide

## ✅ Batch File Fixed!

The `model_interface.bat` file has been fixed and is now working properly.

---

## 🚀 Quick Test

Run this command to verify everything works:

```bash
model_interface.bat help
```

You should see the help menu with all available commands.

---

## 📋 Common Issues & Solutions

### Issue 1: "Python is not installed or not in PATH"

**Solution:**
1. Install Python 3.9+ from https://www.python.org/
2. During installation, check "Add Python to PATH"
3. Restart your terminal/command prompt
4. Verify: `python --version`

### Issue 2: "No module named 'src.model_cli'"

**Solution:**
1. Make sure you're in the TINE directory
2. Install dependencies: `pip install -r requirements.txt`
3. Verify files exist: `dir src\model_cli.py`

### Issue 3: "ModuleNotFoundError: No module named 'torch'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue 4: Batch file doesn't execute

**Solution:**
1. Right-click `model_interface.bat`
2. Select "Run as administrator"
3. Or run from command prompt: `model_interface.bat help`

### Issue 5: "Access is denied"

**Solution:**
1. Open Command Prompt as Administrator
2. Navigate to TINE directory: `cd C:\Users\LENOVO\Desktop\TINE`
3. Run: `model_interface.bat help`

---

## 🧪 Testing the Installation

### Test 1: Check Python
```bash
python --version
```
Should show Python 3.9 or higher.

### Test 2: Check Dependencies
```bash
pip list | findstr torch opencv numpy
```
Should show installed packages.

### Test 3: Check Batch File
```bash
model_interface.bat help
```
Should display help menu.

### Test 4: Check Model Interface
```bash
python -m src.model_cli --help
```
Should display CLI help.

### Test 5: Run Tests
```bash
python -m src.test_model_interface
```
Should run test suite.

---

## 📝 Usage Examples

### Example 1: Show Help
```bash
model_interface.bat help
```

### Example 2: Show Configuration
```bash
model_interface.bat config --show
```

### Example 3: Test Single Image
```bash
model_interface.bat test-single --image test.jpg --output result.png
```

### Example 4: Train Model
```bash
model_interface.bat train --input_dir data\low --gt_dir data\gt
```

### Example 5: Validate Model
```bash
model_interface.bat validate --input_dir data\test_low --gt_dir data\test_gt
```

### Example 6: Test Batch
```bash
model_interface.bat test-batch --input_dir data\test
```

### Example 7: Run Tests
```bash
model_interface.bat test
```

---

## 🔧 Advanced Troubleshooting

### Check Python Path
```bash
where python
```

### Check Current Directory
```bash
cd
```

### List Files in src/
```bash
dir src
```

### Run Python Directly
```bash
python -m src.model_cli train --help
```

### Check Error Details
```bash
python -m src.model_cli train --input_dir data\low --gt_dir data\gt 2>&1
```

---

## 💡 Tips

1. **Always run from TINE directory**
   ```bash
   cd C:\Users\LENOVO\Desktop\TINE
   ```

2. **Use full paths if needed**
   ```bash
   model_interface.bat test-single --image C:\path\to\image.jpg --output C:\path\to\result.png
   ```

3. **Check file permissions**
   - Right-click file → Properties → Security
   - Ensure you have read/write permissions

4. **Use Command Prompt (not PowerShell)**
   - Batch files work better in Command Prompt
   - Open: `cmd.exe`

5. **Keep terminal open to see errors**
   - Don't close terminal immediately after running command
   - Scroll up to see error messages

---

## 📞 Getting Help

### Check Documentation
- `INDEX.md` - Navigation guide
- `QUICK_START.md` - Quick start
- `MODEL_INTERFACE_GUIDE.md` - Complete reference

### Run Help Command
```bash
model_interface.bat help
```

### Check Python CLI Help
```bash
python -m src.model_cli --help
python -m src.model_cli train --help
python -m src.model_cli validate --help
```

### Run Tests
```bash
python -m src.test_model_interface
```

---

## ✅ Verification Checklist

- [ ] Python 3.9+ installed
- [ ] Dependencies installed: `pip install -r requirements.txt`
- [ ] Can run: `model_interface.bat help`
- [ ] Can run: `python -m src.model_cli --help`
- [ ] Can run: `python -m src.test_model_interface`
- [ ] Read QUICK_START.md
- [ ] Tried test-single command
- [ ] Tried train command

---

## 🎯 Next Steps

1. **Verify Installation**
   ```bash
   model_interface.bat help
   ```

2. **Read Quick Start**
   - Open `QUICK_START.md`

3. **Try Test Command**
   ```bash
   model_interface.bat test-single --image test.jpg --output result.png
   ```

4. **Explore Commands**
   - `model_interface.bat train --help`
   - `model_interface.bat validate --help`
   - `model_interface.bat test-batch --help`

---

## 🎉 Success!

If you can run `model_interface.bat help` without errors, everything is working correctly!

**Ready to use the TINE Model Interface! 🚀**
