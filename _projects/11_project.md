---
layout: page
title: Evolutionary Games
description: Designed and developed a 2D Flappy Bird-inspired game with neural networks and evolutionary algorithms.
importance: 1
category: games
img: assets/img/project_preview/helicopter.png
---

This project involved designing and developing a 2D game inspired by Flappy Bird using Python. The core focus was to create a challenging environment for AI agents to learn and adapt using neural networks and evolutionary algorithms.

### Game Design and Implementation

The game was built entirely in Python, with different environments such as **Gravity** and **Thrust**, where each environment presented unique challenges by varying gravity, speed, and obstacles. These diverse scenarios tested the adaptability and robustness of the AI agents. The visual elements, including dynamic obstacles and environment changes, were designed to simulate a challenging but visually appealing gameplay experience.

### AI Design and Training

- **Agent Development:** Hundreds of AI agents were created and trained to play the game. Each agent controlled a virtual helicopter or object, attempting to navigate through obstacles without collisions.
- **Training Mechanism:** 
  - **Neural Networks (NNs):** Each agent used a simple artificial neural network (ANN) to make decisions, such as when to apply thrust or stay idle.
  - **Evolutionary Algorithms:** The agents were optimized using evolutionary algorithms. Agents were scored based on their performance (e.g., distance traveled or obstacles cleared). The top-performing agents "reproduced" by passing their neural network parameters (weights) to the next generation, with random mutations introduced to encourage exploration.
- **Scoring System:** The agents were evaluated and scored dynamically based on their ability to navigate through the varying environments. The scoring mechanism rewarded longer survival and better navigation strategies.

### Game Scenes

<div class="row">
  <div class="col">
    <figure>
      <img src="assets/img/project_preview/helicopter.png" alt="Helicopter Scene" class="img-fluid rounded">
      <figcaption>Helicopter Scene</figcaption>
    </figure>
  </div>
  <div class="col">
    <figure>
      <img src="assets/img/project_preview/gravity.png" alt="Gravity Scene" class="img-fluid rounded">
      <figcaption>Gravity Scene</figcaption>
    </figure>
  </div>
  <div class="col">
    <figure>
      <img src="assets/img/project_preview/thrust.png" alt="Thrust Scene" class="img-fluid rounded">
      <figcaption>Thrust Scene</figcaption>
    </figure>
  </div>
</div>

### Highlights

- Built multiple dynamic game environments with varying levels of difficulty to test AI adaptability.
- Trained AI agents using evolutionary algorithms, producing agents capable of playing the game autonomously with near-perfect accuracy.
- Explored reinforcement learning concepts through iterative evolution and reward systems.

This project not only demonstrated the integration of AI in games but also showcased the potential for creating adaptive agents in dynamic and challenging environments.

[GitHub Repository](https://github.com/bardia-ardakanian/CE351-CI-EvolutionaryGames)
