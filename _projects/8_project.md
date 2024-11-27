---
layout: page
title: Explainable Image Super-Resolution
description: Enhancing SwinIR’s performance with a texture classifier and a novel loss function for better restoration of blurry and noisy images.
importance: 1
category: research
img: assets/img/project_preview/XSWINIR2.png
related_publications: false
github_link: https://github.com/bardia-ardakanian/XSwinIR
---

This project focuses on improving the performance of **SwinIR** for image restoration tasks, particularly for blurry and noisy images, by integrating explainability into the training process. The enhancements include the development of a texture classifier and a novel loss function that emphasizes texture similarity between low-quality inputs and their high-resolution counterparts. These modifications provide not only better restoration performance but also a more interpretable model.

### Key Contributions and Methodology

The central contribution of this project is the integration of a texture classifier into the SwinIR training pipeline. The texture classifier evaluates the similarity between sub-images from low-quality inputs and corresponding regions in high-resolution targets. This similarity measure is used to make the model's decision-making process more interpretable. The lightweight nature of the classifier ensures minimal computational overhead, while its linear design improves transparency.

To further enhance training, a new loss function was introduced, defined as:  
**Loss = SwinIR Loss + min||Xc - y||²**,  
where `Xc` represents the texture classifier's identified sub-image in the high-resolution counterpart, and `y` is the ground truth. This loss function ensures that the restored images retain fine-grained textures, resulting in higher visual quality and better structural preservation.

During training, the SwinIR model leverages the combined loss to focus on key patterns in the data, guided by the texture similarity metric. This approach improves the restoration process for challenging inputs like blurry or noisy images. The iterative nature of the training pipeline refines the model's ability to generalize, ensuring consistent performance across diverse datasets.

### Repository Overview

The complete implementation of this project is available on [GitHub](https://github.com/bardia-ardakanian/XSwinIR). The repository includes training and testing scripts, detailed setup instructions, and all necessary files to replicate the results. It demonstrates how the texture classifier and loss function were integrated into the SwinIR architecture.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project_preview/XSWINIR2.png" title="XSwinIR: Enhanced Image Restoration Framework" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Enhanced XSwinIR framework incorporating explainable texture similarity for improved image restoration.
</div>
