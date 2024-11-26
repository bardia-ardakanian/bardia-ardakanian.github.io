---
layout: page
title: Semi-Supervised Semantic Segmentation
description: Improving semantic segmentation using a multi-phase training strategy and enhanced generative models.
importance: 1
category: research
related_publications: false
github_link: Not available
---

This project builds upon Nvidia's "Semantic Segmentation with Generative Models" by introducing a novel multi-phase training approach and incorporating additional generators and discriminators. These enhancements aim to improve semi-supervised learning, yielding better accuracy and adaptability in semantic segmentation tasks.

### Key Contributions

- **Improved Architecture:**
  - Extended the original model by adding multiple generators and discriminators, enabling more robust semi-supervised learning compared to the original architecture (which used one generator and two discriminators).
  - Increased model flexibility and capacity for handling complex data distributions.

- **Multi-Phase Training Approach:**
  1. **Train the first generator:** Labeled data is used to create a baseline model.
  2. **Train the second generator:** Mixed labeled and unlabeled data are utilized while freezing the first generator.
  3. **Retrain the first generator:** All data (labeled and unlabeled) are used to refine the segmentation performance.
  - This iterative process ensures gradual performance improvement and better adaptability.

### Methodology

- **CycleGAN Integration:**
  - Improved training data diversity using CycleGAN to generate synthetic data, which complements the real dataset.
- **Iterative Refinement:**
  - Repeated optimization cycles leverage both labeled and unlabeled data, making the model more robust and generalizable.

### Features

- Enhancements to Nvidia's Semantic-GAN framework, improving accuracy in semantic segmentation tasks.
- Generated diverse and high-quality synthetic training data with CycleGAN for broader learning coverage.
- Leveraged a semi-supervised learning pipeline to balance limited labeled data with abundant unlabeled data.

### Repository Status

Unfortunately, the repository containing the implementation of this project is currently unavailable.

### Impact

- Enhanced the accuracy and adaptability of semantic segmentation models in semi-supervised settings.
- Improved training efficiency by generating diverse synthetic datasets.
- Provided a scalable solution for tasks requiring high-quality semantic segmentation without extensive labeling.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/project_preview/SemGan.png" title="Semi-Supervised Semantic Segmentation" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Diagram of the GAN cycles and training phases.
</div>