#!/usr/bin/env python
"""
TINE Model Interface - Premium Interactive Menu
An advanced TUI for managing image enhancement workflows.
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

# Initialize Colorama for Windows terminal support
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
except ImportError:
    # Fallback if colorama is not available
    class MockColor:
        def __getattr__(self, name): return ""
    Fore = Back = Style = MockColor()

# Add parent directory to path to ensure src is importable
sys.path.insert(0, str(Path(__file__).parent))

try:
    from src.model_interface import ModelInterface, ModelConfig
    from src.utils import compute_metrics
except ImportError as e:
    print(f"Error: Could not import core components. {e}")
    sys.exit(1)

# --- UI Helpers ---

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}" + "="*65)
    print(f"{Fore.WHITE}{Style.BRIGHT}   ✨ LIGHTFORGE: TINE MODEL RESEARCH INTERFACE ✨")
    print(f"{Fore.CYAN}{Style.BRIGHT}" + "="*65)

def print_header(title):
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}>>> {title}")
    print(f"{Fore.YELLOW}" + "-"*len(title + ">>> "))

def get_input(prompt, default=None):
    if default:
        p = f"{Fore.GREEN}{prompt} {Fore.WHITE}[{default}]: "
    else:
        p = f"{Fore.GREEN}{prompt}: "
    
    val = input(p).strip().strip('"').strip("'")
    return val if val else default

def validate_path(path, is_dir=True):
    if not path:
        return False
    try:
        p = Path(path)
        if is_dir:
            return p.is_dir()
        return p.is_file()
    except Exception:
        return False

def list_suggestions(is_dir=True):
    """List some available items in the current directory to help the user"""
    cwd = Path.cwd()
    if is_dir:
        items = [d.name for d in cwd.iterdir() if d.is_dir() and not d.name.startswith(".")]
        label = "directories"
    else:
        items = [f.name for f in cwd.iterdir() if f.is_file() and f.suffix.lower() in [".jpg", ".png", ".jpeg"]]
        label = "images"
    
    if items:
        print(f"{Fore.CYAN}Available {label} in current folder:")
        for item in items[:10]: # Show top 10
            print(f"  - {item}")
        if len(items) > 10:
            print(f"  ... and {len(items)-10} more")

def print_status(msg, type="info"):
    if type == "success":
        print(f"{Fore.GREEN}[SUCCESS] {msg}")
    elif type == "error":
        print(f"{Fore.RED}[ERROR] {msg}")
    elif type == "warning":
        print(f"{Fore.YELLOW}[WARNING] {msg}")
    else:
        print(f"{Fore.CYAN}[INFO] {msg}")

# --- Menu Actions ---

class InteractiveApp:
    def __init__(self):
        self.interface = ModelInterface()
        self.running = True

    def train(self):
        print_header("1. Hyperparameter Optimization")
        input_dir = get_input("Low-light images directory")
        if not validate_path(input_dir):
            print_status(f"Input directory '{input_dir}' not found.", "error")
            list_suggestions(is_dir=True)
            return

        gt_dir = get_input("Ground truth images directory")
        if not validate_path(gt_dir):
            print_status(f"Ground truth directory '{gt_dir}' not found.", "error")
            list_suggestions(is_dir=True)
            return

        output_dir = get_input("Output directory", "training_logs")
        n_samples = int(get_input("Samples per parameter combo", "10"))

        print_status("Starting hyperparameter search. This may take some time...", "info")
        try:
            results = self.interface.train(input_dir, gt_dir, n_samples=n_samples)
            print_status("Optimization complete!", "success")
            print(f"{Fore.WHITE}Best Parameters: {Fore.CYAN}{results['best_params']}")
            print(f"{Fore.WHITE}Results Logged: {Fore.CYAN}{results['results_file']}")
        except Exception as e:
            print_status(f"Training failed: {e}", "error")

    def validate(self):
        print_header("2. Test Set Evaluation")
        input_dir = get_input("Low-light images directory")
        gt_dir = get_input("Ground truth images directory")
        
        if not validate_path(input_dir) or not validate_path(gt_dir):
            print_status("Invalid data directories.", "error")
            return

        output_dir = get_input("Output results directory", "validation_results")
        
        print_status("Running validation suite...", "info")
        try:
            stats = self.interface.validate(input_dir, gt_dir, output_dir=output_dir)
            print_status("Validation complete!", "success")
            print(f"{Fore.WHITE}Mean PSNR: {Fore.GREEN}{stats['psnr']['mean']:.2f} dB")
            print(f"{Fore.WHITE}Mean SSIM: {Fore.GREEN}{stats['ssim']['mean']:.4f}")
        except Exception as e:
            print_status(f"Validation failed: {e}", "error")

    def test_single(self):
        print_header("3. Test Single Image")
        img_path = get_input("Image path")
        if not validate_path(img_path, is_dir=False):
            print_status(f"Image file '{img_path}' not found.", "error")
            list_suggestions(is_dir=False)
            return

        out_name = f"enhanced_{Path(img_path).name}"
        output_path = get_input("Output path", out_name)

        print_status("Enhancing image...", "info")
        try:
            self.interface.test_single(img_path, output_path)
            print_status(f"Image saved to {output_path}", "success")
        except Exception as e:
            print_status(f"Processing failed: {e}", "error")

    def test_batch(self):
        print_header("4. Test Batch of Images")
        input_dir = get_input("Input images directory")
        if not validate_path(input_dir):
            print_status(f"Input directory '{input_dir}' not found.", "error")
            list_suggestions(is_dir=True)
            return

        output_dir = get_input("Output directory", "batch_test_results")
        compare = get_input("Compare with baselines? (y/n)", "y").lower() == "y"

        print_status(f"Processing batch from {input_dir}...", "info")
        try:
            summary = self.interface.test(input_dir, output_dir, compare_baselines=compare)
            print_status(f"Batch complete! Success: {summary['successful']}/{summary['total_images']}", "success")
        except Exception as e:
            print_status(f"Batch processing failed: {e}", "error")

    def show_config(self):
        print_header("5. Current Configuration")
        config = self.interface.get_config()
        for k, v in config.items():
            print(f"{Fore.CYAN}{k:<20}: {Fore.WHITE}{v}")

    def save_config(self):
        print_header("6. Save Configuration")
        path = get_input("Path to save config (JSON)", "config_current.json")
        try:
            saved_path = self.interface.save_config(path)
            print_status(f"Configuration saved to {saved_path}", "success")
        except Exception as e:
            print_status(f"Save failed: {e}", "error")

    def load_config(self):
        print_header("7. Load Configuration")
        path = get_input("Path to config file (JSON)")
        if not validate_path(path, is_dir=False):
            print_status("Config file not found.", "error")
            return
        
        try:
            import json
            with open(path, "r") as f:
                config_dict = json.load(f)
            self.interface.update_config(**config_dict)
            print_status("Configuration loaded successfully!", "success")
        except Exception as e:
            print_status(f"Load failed: {e}", "error")

    def run_benchmark(self):
        print_header("8. Comprehensive Benchmark")
        input_dir = get_input("Input directory")
        gt_dir = get_input("GT directory")
        
        if not validate_path(input_dir) or not validate_path(gt_dir):
            print_status("Data paths are required for benchmarking.", "error")
            return

        print_status("Starting full benchmark pipeline (Train -> Validate)...", "info")
        try:
            # Re-implementing the CLI benchmark logic here for direct access
            train_results = self.interface.train(input_dir, gt_dir)
            best_params = train_results["best_params"]
            
            print_status("Updating model with optimal parameters...", "info")
            self.interface.update_config(**best_params)
            
            print_status("Final validation run...", "info")
            val_stats = self.interface.validate(input_dir, gt_dir, output_dir="benchmark_results")
            
            print_status("Benchmark Final Results:", "success")
            print(f"{Fore.WHITE}Optimal PSNR: {Fore.GREEN}{best_params['avg_psnr']:.2f} dB")
            print(f"{Fore.WHITE}Optimal SSIM: {Fore.GREEN}{best_params['avg_ssim']:.4f}")
        except Exception as e:
            print_status(f"Benchmark failed: {e}", "error")

    def run_tests(self):
        print_header("9. Run Unit Tests")
        print_status("Executing core test suite...", "info")
        try:
            import unittest
            # Use the existing test file
            from src.test_model_interface import TestModelInterface
            suite = unittest.TestLoader().loadTestsFromTestCase(TestModelInterface)
            runner = unittest.TextTestRunner(verbosity=1)
            result = runner.run(suite)
            if result.wasSuccessful():
                print_status("All core tests passed!", "success")
            else:
                print_status(f"Tests failed: {len(result.failures)} failures, {len(result.errors)} errors", "error")
        except Exception as e:
            print_status(f"Test execution failed: {e}", "error")

    def exit(self):
        print(f"\n{Fore.CYAN}Exiting LightForge Interface. Goodbye!{Style.RESET_ALL}")
        self.running = False

    def run(self):
        clear_screen()
        while self.running:
            print_banner()
            print(f"{Fore.WHITE} [1]  {Fore.CYAN}Train (Hyperparameter Search)")
            print(f"{Fore.WHITE} [2]  {Fore.CYAN}Validate (Test Set Evaluation)")
            print(f"{Fore.WHITE} [3]  {Fore.CYAN}Test Single Image")
            print(f"{Fore.WHITE} [4]  {Fore.CYAN}Test Batch of Images")
            print(f"{Fore.WHITE} [5]  {Fore.CYAN}Show Configuration")
            print(f"{Fore.WHITE} [6]  {Fore.CYAN}Save Configuration")
            print(f"{Fore.WHITE} [7]  {Fore.CYAN}Load Configuration")
            print(f"{Fore.WHITE} [8]  {Fore.CYAN}Run Full Benchmark")
            print(f"{Fore.WHITE} [9]  {Fore.CYAN}Run Core Tests")
            print(f"{Fore.WHITE} [10] {Fore.RED}Exit")
            print(f"{Fore.CYAN}" + "="*65)
            
            choice = get_input("Selection (1-10)")
            
            actions = {
                "1": self.train,
                "2": self.validate,
                "3": self.test_single,
                "4": self.test_batch,
                "5": self.show_config,
                "6": self.save_config,
                "7": self.load_config,
                "8": self.run_benchmark,
                "9": self.run_tests,
                "10": self.exit
            }
            
            if choice in actions:
                actions[choice]()
                if self.running:
                    input(f"\n{Fore.WHITE}Press Enter to return to menu...")
                    clear_screen()
            else:
                print_status("Invalid selection.", "error")
                time.sleep(1)
                clear_screen()

if __name__ == "__main__":
    app = InteractiveApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Interrupted by user. Shutting down.")
        sys.exit(0)
