import sys
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from pathlib import Path

# Ensure repo root and src/ are on sys.path so local package imports work in varied environments
repo_root = Path(__file__).parent.resolve()
repo_root_str = str(repo_root)
src_path = str(repo_root / "src")
if repo_root_str not in sys.path:
    sys.path.insert(0, repo_root_str)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Attempt to import core implementation from src/. If missing, show a friendly error in the UI
try:
    from src.multiscale_artifact_reduction import (
        multi_scale_feature_extraction,
        baseline_clahe,
        baseline_gamma_correction,
        baseline_edge_preserving
    )
    from src.utils import compute_metrics
    from src.dncnn import get_dncnn_model
    from src.model_interface import ModelInterface, ModelConfig
    SRC_AVAILABLE = True
    SRC_IMPORT_ERROR = None
except Exception as e:
    SRC_AVAILABLE = False
    SRC_IMPORT_ERROR = e

import torch

# Cached loader for DL model (if available)
@st.cache_resource
def load_dl_model():
    if not SRC_AVAILABLE:
        return None, "cpu"
    # Show a spinner while the model is loading
    with st.spinner("Loading Pre-trained DnCNN Model..."):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        try:
            return get_dncnn_model(device=device), device
        except Exception as e:
            # Surface a friendly error if model init fails
            st.error(f"Failed to initialize DnCNN model: {e}")
            return None, "cpu"

st.set_page_config(page_title="LightForge", layout="wide", page_icon="✨")

# If core src package isn't available, show an error and stop execution early to avoid crashes
if not SRC_AVAILABLE:
    st.title("✨ LightForge: Multi-Scale Image Enhancement")
    st.error(
        "The application cannot import required modules from the `src` package.\n"
        "Possible causes:\n"
        " - You are running the app from a checkout that does not include the `src/` directory.\n"
        " - The Python path is misconfigured and cannot find the local `src` package.\n\n"
        f"Original import error: {SRC_IMPORT_ERROR}"
    )
    st.info("To fix: ensure the repository contains the `src/` folder (with files like multiscale_artifact_reduction.py, utils.py, dncnn.py) or install the package into your environment.\n"
            "If you're deploying on Streamlit Cloud, include the src files in the repo and re-deploy.")
    st.stop()

# Custom CSS for a premium look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2c3e50;
        font-family: 'Inter', sans-serif;
    }
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3498db, #8e44ad);
    }
    .css-1d391kg {
        background-color: #2c3e50;
    }
</style>
""", unsafe_allow_html=True)

st.title("✨ LightForge: Multi-Scale Image Enhancement")
st.markdown("A premium, real-time research tool for reducing artifacts and enhancing details in low-light photography and medical imaging.")
st.markdown("---")

st.sidebar.title("Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload Low-Light Image", type=["jpg", "jpeg", "png"])
gt_file = st.sidebar.file_uploader("Upload Ground Truth (Optional)", type=["jpg", "jpeg", "png"])

st.sidebar.markdown("### Algorithm Parameters")
denoise_method = st.sidebar.radio("Denoising Method", ["Deep Learning (DnCNN)", "Non-Local Means (OpenCV)"])
levels = st.sidebar.slider("Pyramid Levels", min_value=1, max_value=6, value=4)
denoise_strength = st.sidebar.slider("Denoising Strength (NLM only)", min_value=0, max_value=50, value=10)
detail_strength = st.sidebar.slider("Detail Strength", min_value=0.0, max_value=2.0, value=0.8, step=0.1)
gamma = st.sidebar.slider("Gamma Correction", min_value=0.1, max_value=2.0, value=0.75, step=0.05)
clahe_clip = st.sidebar.slider("CLAHE Clip Limit", min_value=1.0, max_value=5.0, value=2.0, step=0.1)

st.sidebar.markdown("---")
show_baselines = st.sidebar.checkbox("Generate Baseline Comparisons", value=False)

def process_image(image):
    # Ensure image is RGB (3 channels) so that cv2 functions expecting colored images work correctly
    if image.mode != "RGB":
        image = image.convert("RGB")
    return np.array(image)

# Main UI with Tabs
tab1, tab2 = st.tabs(["🚀 Enhancement", "🧠 Training Hub"])

with tab1:
    st.markdown("### Interactive Enhancement")
    if uploaded_file is not None:
        original_pil = Image.open(uploaded_file)
        original = process_image(original_pil)
        
        st.markdown("### Enhancement Results")
        
        with st.spinner("Processing..."):
            if denoise_method == "Deep Learning (DnCNN)":
                dl_model, device = load_dl_model()
            else:
                dl_model, device = None, "cpu"

            enhanced = multi_scale_feature_extraction(
                original,
                levels=levels,
                denoise_strength=denoise_strength,
                detail_strength=detail_strength,
                gamma=gamma,
                clahe_clip=clahe_clip,
                dl_model=dl_model,
                device=device
            )
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(original, caption="Original Low-Light Image", use_container_width=True)
        with col2:
            st.image(enhanced, caption="Enhanced Image (Proposed Method)", use_container_width=True)

        if gt_file is not None:
            gt_pil = Image.open(gt_file)
            gt = process_image(gt_pil)
            
            psnr, ssim = compute_metrics(gt, enhanced)
            st.success(f"**Metrics vs Ground Truth:** PSNR = {psnr:.2f} dB | SSIM = {ssim:.4f}")
            
        if show_baselines:
            st.markdown("---")
            st.markdown("### Baseline Comparisons")
            with st.spinner("Generating baselines..."):
                clahe_res = baseline_clahe(original, clip_limit=clahe_clip)
                gamma_res = baseline_gamma_correction(original, gamma=gamma)
                edge_res = baseline_edge_preserving(original)
                
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.image(clahe_res, caption="CLAHE Baseline", use_container_width=True)
                with c2:
                    st.image(gamma_res, caption="Gamma Correction Baseline", use_container_width=True)
                with c3:
                    st.image(edge_res, caption="Edge Preserving Filter Baseline", use_container_width=True)
    else:
        st.info("⬅️ Please upload an image from the Control Panel to get started.")

with tab2:
    st.markdown("### Hyperparameter Optimization")
    st.markdown("Find the optimal settings for your specific dataset automatically.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        train_input_dir = st.text_input("Low-light Images Directory", value="data/low")
    with col_b:
        train_gt_dir = st.text_input("Ground Truth Images Directory", value="data/gt")
    
    train_n_samples = st.number_input("Samples per parameter combo", min_value=1, max_value=90, value=5)
    
    if st.button("🔥 Start Optimization"):
        if not (Path(train_input_dir).is_dir() and Path(train_gt_dir).is_dir()):
            st.error("Invalid directories. Please check the paths.")
        else:
            interface = ModelInterface()
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Use the new progress callback feature
            status_text.info(f"Starting search on {train_n_samples} samples per combination...")
            
            def update_progress(progress):
                progress_bar.progress(progress)
                status_text.text(f"Progress: {progress*100:.1f}%")

            try:
                results = interface.train(
                    train_input_dir, 
                    train_gt_dir, 
                    n_samples=train_n_samples,
                    progress_callback=update_progress
                )
                
                progress_bar.empty()
                status_text.empty()
                st.success("Optimization Complete!")
                
                best = results["best_params"]
                st.markdown("#### 🏆 Best Parameters Found")
                
                c1, c2, c3, c4 = st.columns(4)
                c1.metric("Levels", best["levels"]) 
                c2.metric("Detail Strength", best["detail_strength"])
                c3.metric("Gamma", best["gamma"])
                c4.metric("CLAHE Clip", best["clahe_clip"])
                
                st.metric("Top Average PSNR", f"{best['avg_psnr']:.2f} dB")
                st.metric("Top Average SSIM", f"{best['avg_ssim']:.4f}")
                
                with st.expander("Detailed Results JSON"):
                    st.json(results)
                
                st.info(f"Full results saved to: {results['results_file']}")
            except Exception as e:
                st.error(f"Training failed: {e}")
