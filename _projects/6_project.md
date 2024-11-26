---
layout: page
title: Deep Active Learning Object Detection
description: Enhancing Single Shot MultiBox Detector (SSD) training efficiency using deep active learning approaches.
img: assets/img/project_preview/ALVAE2.png
importance: 1
category: research
related_publications: true
github_link: https://github.com/bardia-ardakanian/AL-VAE
---

This project focuses on **improving the training process of the Single Shot MultiBox Detector (SSD)** by integrating a deep active learning framework. The method filters out the most informative images from the dataset, reducing manual labeling efforts while improving the model's performance.

### Key Contributions

- **Active Learning Framework:**
  - Developed a dual-scoring system that combines **Variant Autoencoder (VAE) reconstruction loss** and SSD detector loss to rank and prioritize images.
  - Utilized fixed weights on unlabeled data for consistent and effective image selection.

- **Efficient Data Utilization:**
  - Reduced manual labeling requirements by focusing on the most informative samples from the **unlabeled pool**.
  - Implemented a **sorting function** to systematically improve the quality of data used for training.

### Methodology

- **Variant Autoencoder (VAE):**
  - Used VAE to analyze and reconstruct images, calculating a reconstruction loss as a measure of informativeness.
  - This loss, combined with SSD detection loss, allowed effective ranking of images for training.

- **Iterative Training:**
  - Curated and updated the labeled dataset iteratively through active learning.
  - Focused training on high-priority samples identified by the scoring system, improving efficiency.

### Features

- **Variational Autoencoder (VAE):**
  - Evaluates the information content of images to assess their potential for enhancing model training.
- **Active Learning:**
  - Focuses on selecting data samples that provide the highest impact on SSD training.
- **Dual-Scoring System:**
  - Combines metrics from VAE and SSD to rank and select the most useful images.

### Impact

- Reduced the overall labeling workload by selectively training on key samples.
- Achieved better accuracy and faster convergence for SSD training.
- Made the framework scalable for large datasets, enabling practical applications in object detection.

### GitHub Repository

Explore the PyTorch implementation and codebase for this project on [GitHub](https://github.com/bardia-ardakanian/AL-VAE). The repository includes setup instructions, source code, and detailed documentation.

### Related Publications

- **Bardia Ardakanian**, "Development of Natural and Artificial Intelligence - Post-Selection Dialogue: Challenges to Post-Selection," *IEEE Cognitive Development Systems Newsletter*, vol. 18, no. 2, pp. 6–11, 2024.  
  [Read Online](https://www.cse.msu.edu/amdtc/amdnl/CDSNL-V18-N2.pdf#page=6) | [PDF](assets/pdf/CDSNL-V18-N2.pdf)

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project_preview/ALVAE.png" title="Deep Active Learning Framework for SSD" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Diagram of the deep active learning framework applied to SSD training.
</div>
