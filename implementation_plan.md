# Deep Learning Denoising Integration Plan

This plan outlines the steps to fetch a pre-trained Deep Convolutional Neural Network (DnCNN) from the internet and integrate it natively into the Multi-Scale Artifact Reduction pipeline. DnCNN is considered a gold standard for grayscale medical image (CT/X-Ray) denoising.

## User Review Required

> [!IMPORTANT]
> Please review this architecture. I have chosen the renowned **DnCNN** architecture with weights pre-trained on grayscale images (which perfectly matches CT and X-ray modalities). 
> The weights will be downloaded automatically from the author's public repository (`cszn/KAIR`) on the first run.

## Open Questions

- Should the Deep Learning denoising *completely replace* the current Non-Local Means (NLM) algorithm, or would you prefer a toggle in the UI so you can switch between them and compare? I will add a toggle by default.
- Does your hardware support CUDA (NVIDIA GPU)? The plan implements it to automatically use the GPU if available, falling back to CPU otherwise.

## Proposed Changes

### Core Implementation

#### [NEW] `src/dncnn.py`
Create the PyTorch network architecture for DnCNN.
- Implementing the 17-layer (Conv+ReLU, 15x Conv+BN+ReLU, Conv) network.
- Add utility functions to download the `dncnn_gray_blind.pth` weights automatically.

#### [MODIFY] `src/multiscale_artifact_reduction.py`
- Add a new function `dncnn_denoise(image, model, device)` which takes a PyTorch model and performs inference on the input image scale.
- Update `multi_scale_feature_extraction` to accept an optional `dl_model` parameter. If provided, the pyramid layers will be denoised using the neural network instead of OpenCV's NLM.

#### [MODIFY] `app.py`
- Add a UI control to select the Denoising Method ("Deep Learning (DnCNN)" vs "Non-Local Means").
- Add caching logic (`@st.cache_resource`) to load the PyTorch model once into memory.
- Pass the loaded model into the extraction pipeline.

## Verification Plan

### Automated/Manual Testing
- I will verify the automatic downloading of the `.pth` file using PyTorch's hub utilities.
- I will execute the Streamlit app and perform inference using the Deep Learning model to ensure the tensor conversions (NumPy -> PyTorch Tensor -> NumPy) don't introduce artifacts.
- I will verify the visual output on the generated test image.
