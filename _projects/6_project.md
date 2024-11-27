---
layout: page
title: Deep Active Learning Object Detection
description: Improving Single Shot MultiBox Detector (SSD) training with an advanced active learning framework.
img: assets/img/project_preview/ALVAE2.png
importance: 1
category: research
related_publications: true
github_link: https://github.com/bardia-ardakanian/AL-VAE
---

This project focuses on **enhancing the training process of the Single Shot MultiBox Detector (SSD)** through the integration of a deep active learning framework. By prioritizing the most informative images from a pool of unlabeled data, the framework significantly reduces manual labeling efforts while improving model accuracy and efficiency.

### Key Contributions and Methodology

At the core of this framework is a **dual-scoring system** that evaluates the informativeness of each image using two complementary loss metrics: the **reconstruction loss** from a Variational Autoencoder (VAE) and the **detection loss** from the SSD model. The VAE analyzes and reconstructs input images, with its reconstruction loss (`L_reconstruction`) serving as a measure of how unique or underexplored an image is in the dataset. Images with higher reconstruction loss are flagged as potentially valuable for training, as they represent regions of the data distribution that the model has yet to fully understand.

Simultaneously, the SSD model evaluates each image’s **detection loss** (`L_detection`), which reflects how much the image can contribute to improving object detection accuracy. These two metrics are combined into a single scoring function:  
**Score = α × L_reconstruction + β × L_detection**,  
where `α` and `β` are weights used to balance the importance of the VAE and SSD contributions. This scoring function ranks images, enabling the system to prioritize the most impactful ones for labeling and subsequent training.

The framework operates iteratively, selecting and labeling the highest-ranked images in each cycle. As new data is incorporated, the SSD model’s performance improves progressively, while the VAE continues to identify novel and diverse samples from the unlabeled pool. This iterative approach ensures efficient use of limited labeling resources while achieving rapid convergence and improved detection performance.

### Technical Impact

By strategically filtering and prioritizing images, the framework significantly reduces the time and cost associated with manual labeling. It scales efficiently to large datasets, making it a practical solution for real-world object detection challenges. The combination of the VAE and SSD enables the system to balance novelty and utility in data selection, resulting in faster training and higher model accuracy.

### GitHub Repository

The full PyTorch implementation and documentation are available on [GitHub](https://github.com/bardia-ardakanian/AL-VAE). This repository provides all necessary resources for reproducing the results and adapting the framework to other object detection tasks.

### Related Publications

- **Bardia Ardakanian**, "Development of Natural and Artificial Intelligence - Post-Selection Dialogue: Challenges to Post-Selection," *IEEE Cognitive Development Systems Newsletter*, vol. 18, no. 2, pp. 6–11, 2024.  
  [Read Online](https://www.cse.msu.edu/amdtc/amdnl/CDSNL-V18-N2.pdf#page=6) | [PDF](assets/pdf/CDSNL-V18-N2.pdf)

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project_preview/ALVAE2.png" title="Deep Active Learning Framework for SSD" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Framework integrating VAE and SSD for active learning in object detection.
</div>
