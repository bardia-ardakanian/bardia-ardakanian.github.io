---
layout: page
title: Soft-Margin SVM
description: Reformulated Soft-Margin SVM as a linear optimization problem and implemented it using Pyomo.
importance: 2
category: research
img: assets/img/project_preview/smsvm.png
---

This project involved reformulating the **Soft-Margin Support Vector Machine (SVM)** problem into a **linear optimization framework**, enabling its implementation using **Pyomo**, a Python-based optimization modeling language. The reformulation allowed the **slack variable** to dynamically adapt based on the separation properties of the dataset, such as whether the data was fully separable or significantly overlapped.

### Soft-Margin SVM Formulation

The standard Soft-Margin SVM problem is formulated as:

\[
\min_{w, b, \xi} \frac{1}{2} \|w\|^2 + C \sum_{i=1}^n \xi_i
\]
\[
\text{subject to: } y_i (w \cdot x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0 \text{ for } i = 1, \dots, n
\]

Here:
- \(w\) is the weight vector defining the decision boundary.
- \(b\) is the bias term.
- \(\xi_i\) are the slack variables allowing misclassification.
- \(C\) is the regularization parameter controlling the trade-off between margin size and misclassification tolerance.

### Reformulated as a Linear Optimization Problem

The SVM problem can be reformulated into a linear optimization problem by representing the quadratic term \(\frac{1}{2} \|w\|^2\) using constraints on an auxiliary variable \(z\). The linearized version becomes:

\[
\min_{w, b, \xi, z} z + C \sum_{i=1}^n \xi_i
\]
\[
\text{subject to: } \|w\|^2 \leq z, \quad y_i (w \cdot x_i + b) \geq 1 - \xi_i, \quad \xi_i \geq 0
\]

This formulation transforms the quadratic minimization into a linear problem, which is easier to solve using optimization libraries like Pyomo.

### Implementation and Results

Using Pyomo, I modeled the linearized problem and implemented a solution pipeline. The slack variables \(\xi_i\) were optimized to reflect the separability of the dataset:
- For fully separable data, \(\xi_i = 0\) for most points, yielding a large margin.
- For highly overlapped data, larger values of \(\xi_i\) allowed for flexibility in the decision boundary.

The reformulated problem worked efficiently across datasets, with performance varying based on the level of separability in the data. This approach demonstrated how optimization techniques could be leveraged to solve machine learning problems in a structured and adaptable way.

[GitHub Repository](https://github.com/bardia-ardakanian/CS183-SMSVM-Pyomo)
