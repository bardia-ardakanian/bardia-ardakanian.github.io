---
layout: page
title: Stock Market Sentiment Analysis Botnet
description: Built a botnet for crowdsourced sentiment analysis of stock market data.
importance: 1
category: fun
img: assets/img/project_preview/crowdsource.png
---

This project involved building a botnet to perform **crowdsourced sentiment analysis** of stock market data from platforms like **Twitter** and **Reddit**. The system began by scraping data through APIs, which I studied extensively to design custom scripts for collecting relevant posts and comments. The scraped data was then processed using **Natural Language Processing (NLP)** techniques to classify social media sentiment into actionable signals, such as "buy" or "sell."

To fully automate the process, I developed a bot that ran periodically every 30 minutes. The bot fetched the latest data, analyzed it, and published the generated signals to a **Telegram channel** for real-time updates. Additionally, I evaluated the signals' accuracy by comparing them against actual stock price movements. This feedback loop provided a way to refine my sentiment analysis model and measure its effectiveness.

[GitHub Repository](https://github.com/Computer-Engineering-Department-Archive/CE307-SE1-C3PO)
