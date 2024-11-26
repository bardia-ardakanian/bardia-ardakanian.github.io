---
layout: page
title: Explainable Image Super-Resolution
description: Improving SwinIR's performance with a texture classifier and a new loss function for better restoration of blurry and noisy images.
importance: 1
category: research
img: assets/img/project_preview/XSWINIR2.png
related_publications: false
github_link: https://github.com/bardia-ardakanian/XSwinIR
---

We have developed a **PyTorch implementation of SwinIR** and enhanced it to improve performance on blurry and noisy images. The core idea includes integrating a **texture classifier** and a novel loss function to guide the training process by focusing on the similarity between sub-images in low-quality inputs and their high-resolution counterparts.

### Key Contributions

- **Texture Classifier:**
  - Designed to evaluate the similarity between sub-images, enabling a more explainable and interpretable training process.
  - Incorporates a **linear nature**, enhancing the model's transparency.

- **New Loss Function:**
  - Introduced a new loss formula: **SwinIR loss + min||Xc - y||²**, where:
    - `Xc` represents similar sub-images in the high-quality image corresponding to the current sub-image in the low-quality input.
    - `y` is the target high-resolution counterpart.
  - This loss focuses on preserving texture similarity, resulting in better restoration performance.

- **Performance Improvements:**
  - Enhanced SwinIR's ability to restore blurry and noisy images by integrating explainability into the training process.

### Methodology

1. **Texture Classification:**
   - A lightweight classifier identifies and matches sub-images from high-resolution images to low-quality inputs.

2. **Training Process:**
   - The SwinIR model is trained with the new loss function, combining the base SwinIR loss with the texture similarity term.

3. **Explainability Focus:**
   - The explainable nature of the texture classifier guides the model to focus on specific patterns, improving restoration quality.

### Training and Testing Instructions

#### Training
1. Use `main_train_psnr.py` with the following arguments:
   - `--opt`: Specify the configuration option file.
   - `--tensorboard`: Enable TensorBoard for visualization.

2. Preprocess the training data:
   - Run `generate_mod_LR_bic.py` on high-resolution images to generate low-resolution counterparts.
   - Extract sub-images using `extract_subimages.py` for HR and LR folders.

#### Testing
1. Use `main_test_swinir.py` with the following arguments:
   - `--scale`: Define the scaling factor.
   - `--training_patch_size`: Specify the patch size for testing.
   - `--model_path`: Provide the path to the trained model.
   - `--folder_lq`: Point to the folder with low-quality inputs.
   - `--folder_gt`: Specify the folder with ground-truth images.

2. For benchmarks:
   - Download benchmarks using `python download_benchmarks.py zip_url destination_folder`.

### Repository Overview

The codebase is available on [GitHub](https://github.com/bardia-ardakanian/XSwinIR). Below is the directory structure:

- **`data/`**: Contains dataset-related scripts (e.g., `dataset_sr` for super-resolution).
- **`models/`**: Includes model definitions and core architecture. Add your network to `select_network.py` and update `model_plain.py` for training-specific modifications.
- **`options/`**: Stores training configuration files.
- **Scripts/`: Scripts for data preparation and benchmarks.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project_preview/XSWINIR.png" title="XSwinIR: Enhanced Image Restoration Framework" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Improved XSwinIR framework integrating texture similarity for better image restoration.
</div>
