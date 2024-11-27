---
layout: page
title: XTC Texture Classifier
description: A machine learning model for identifying similar sub-images using VGG16 and linear regression.
importance: 2
category: research
img: assets/img/project_preview/XTC.png
---

The XTC Texture Classifier is part of a broader research effort in image super-resolution, aiming to identify high-quality sub-images similar to a low-quality input. The system uses the **VGG16** model, a pre-trained convolutional neural network, to extract high-level features from sub-images. These features are passed through a lightweight linear regression model, which computes similarity scores to find matches between low-resolution inputs and high-resolution target sub-images.

To align with its intended use case, the training process involves scaling down input images to mimic low-quality conditions. The model is trained on the **DIV2K** dataset, leveraging its high-resolution images to capture intricate texture patterns. By learning to map low-quality inputs to their high-quality counterparts, the classifier achieves a 95% accuracy rate.

[GitHub Repository](https://github.com/bardia-ardakanian/XTC/tree/main)
