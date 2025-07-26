# IQ-UltraRecon: Demodulated IQ Ultrasound Dataset of Human Hand and Arm Tissue
## Overview
This repository contains the IQ-UltraRecon dataset, which includes demodulated in-phase (I) and quadrature (Q) ultrasound data captured from the human hand and forearm. The dataset was acquired using a Verasonics Vantage 64LE ultrasound system and is intended for deep learning-based reconstruction and analysis. The data is available in MATLAB .mat format and comprises both single-angle and multi-angle acquisitions.

The goal of this dataset is to support research in ultrasound signal analysis, beamforming alternatives, and deep learning-based image reconstruction. It can be used for a variety of applications, including the development of signal-to-image networks, adaptive beamformers, and phase-aware reconstructions.

## Key Features
### Demodulated IQ Data: 
The dataset includes raw in-phase and quadrature signal components, preserving their amplitude and phase information.

### Multiple Acquisition Angles: 
It includes both single-angle and multi-angle acquisitions, enabling advanced signal analysis and comparison.

### Format: 
All files are in .mat format, compatible with both Python and MATLAB environments.

### Size: 
The dataset contains 48 .mat files with a total of 4,800 data samples.

## Dataset Description

### The data is organized into the following types:
i. Single-angle data (I and Q components): Contains a single-frame (1, 1, 256, 256) for both I and Q components.

ii. Multi-angle data (I and Q components): Contains sequences of frames (400, 1, 256, 256), each corresponding to different insonification angles.

### Example file names:
240819_EH_01_01_100_im.mat — In-phase, multi-angle data.

240819_EH_01_01_100_qs.mat — Quadrature, single-angle data.

## Data Accessibility
The dataset is publicly available through Mendeley Data:

Repository Name: Mendeley Data

Data DOI: 10.17632/tm9tjpg542.1

## Data Preprocessing
### Preprocessing Steps:

i. Axis Standardization: Ensure consistent axis order based on your deep learning framework (PyTorch or TensorFlow).

ii. Normalization: Scale the pixel values to a uniform range (e.g., [0, 1]) or apply Z-score normalization.

iii. Logarithmic Compression: Applied to magnitude signals to reduce dynamic range and improve perceptual contrast for image-based processing.

iv. Frame Selection: Specific frames can be selected from multi-angle data for various applications.

## Recommended Deep Learning Algorithms:

IQ-to-B-mode Image Reconstruction: Use U-Net, ResU-Net, or Dense U-Net.

Super-Resolution: Utilize ESRGAN, SwinIR, or 3D U-Net models.

Denoising: Train models like DnCNN and FFDNet using noisy-clean frame pairs.

Angular Feature Learning: Use RNNs or TCNs for modeling dependencies across angular views.

## Limitations
i. Sample Diversity: Data acquired from healthy adult volunteers under controlled conditions. There is no pathological data in the current release.

ii. Insonification Angles: The angles are confined to a ±15° sector, which may not represent the full clinical probe steering range.

iii. Transducer Characteristics: Data is limited to a single transducer model (L11-5v), which may limit variability for certain studies.

## Ethics Statement
This dataset was acquired as part of a study approved by the IRB of Pusan National University (Protocol No. PNU-2025-001). All volunteers provided written informed consent, and the data were anonymized before sharing.
