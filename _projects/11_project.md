---
layout: page
title: Evolutionary Games
description: Designed and developed a 2D Flappy Bird-inspired game with neural networks and evolutionary algorithms.
importance: 1
category: games
img: assets/img/project_preview/helicopter.png
---

This project involved designing and developing a **2D game inspired by Flappy Bird** entirely in **Python**. My goal was to learn both **game design** and how to train **AI agents** within a game environment. Using the **Game2D** library, I created dynamic scenarios like **Gravity** and **Thrust**, which introduced varying gravity, speed, and obstacle layouts. These challenges made the game a suitable environment for testing the adaptability and decision-making abilities of AI-controlled agents.

The game uses **artificial neural networks (ANNs)** and **evolutionary algorithms** to train AI agents. I implemented a system where hundreds of agents attempt to navigate the game environment simultaneously, each receiving a score based on their performance, such as distance traveled or obstacles cleared. The best-performing agents were selected for the next generation, while their **neural network weights** were passed on with random **mutations** to introduce variability. This process continued until an agent either completed the game or achieved stable, high-level performance.

### Game Scenes

<div class="row justify-content-sm-center">
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/project_preview/helicopter.png" title="Helicopter Scene" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/project_preview/gravity.png" title="Gravity Scene" class="img-fluid rounded z-depth-1" %}
  </div>
  <div class="col-sm-4 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/project_preview/thrust.png" title="Thrust Scene" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

### Training Visualization

<div class="row justify-content-sm-center">
  <div class="col-sm-8 mt-3 mt-md-0">
    {% include figure.liquid path="assets/img/project_preview/helicopter_many.png" title="Training Scene with Hundreds of AI-Controlled Helicopters" class="img-fluid rounded z-depth-1" %}
  </div>
</div>

This project was a hands-on experience in learning how to design interactive systems and develop AI agents that adapt to changing conditions. By building the game from scratch and training the agents with **evolutionary algorithms**, I gained a deeper understanding of how AI can be used in game environments to solve complex challenges.

[GitHub Repository](https://github.com/bardia-ardakanian/CE351-CI-EvolutionaryGames)
