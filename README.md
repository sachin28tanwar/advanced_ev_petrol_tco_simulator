# Advanced EV vs. Petrol TCO Simulator (EnergyVerse ⚡)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://advancedevpetroltcosimulator-md7gj3txjvdjsdohwqvaug.streamlit.app/)

## Project Overview
This project is an **Advanced EV vs. Petrol TCO (Total Cost of Ownership) Simulator**. It is a deep-dive simulator accounting for inflation, maintenance, insurance, and battery degradation to model cumulative cost trajectories over years of ownership.

It is part of the **EnergyVerse** ecosystem: a full-stack data analytics platform designed to monitor, predict, and optimize a modern city's energy ecosystem. As urban environments grow, managing power efficiently becomes critical. This project tackles city-wide energy challenges by transforming raw energy data into actionable insights for citizens, grid operators, and city planners.

## Project Structure
EnergyVerse is divided into three distinct modules scaled by technical complexity (Easy, Medium, and Hard). While each module focuses on a different urban energy problem, they all share a unified technical pipeline:
* **Data Processing:** SQL is used to extract, aggregate, and analyze large-scale urban datasets.
* **Predictive Analytics:** Machine Learning models are deployed to forecast demand, detect anomalies, or optimize resources.
* **Interactive UI:** Streamlit web applications serve as the front-end, turning complex models into user-friendly, interactive dashboards.

## The Three Modules
1. **Level 1 (Foundational Analysis):** Focuses on historical consumption and benchmarking. Example: Tracking residential energy usage and calculating the municipal carbon footprint.
2. **Level 2 (Predictive Modeling):** Focuses on forecasting and anomaly detection. Example: Predicting peak grid loads to prevent outages or assessing neighborhood solar potential. 
3. **Level 3 (System Optimization - This Simulator):** Focuses on dynamic, real-time resource allocation and economic simulations. Example: Optimizing the charging schedules for public EV fleets, simulating automated load-shedding during extreme weather crises, or modeling the total cost of ownership (TCO) comparison.

## How to Run the Simulator
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## Core Objective
To demonstrate a complete end-to-end data science workflow—from database management to machine learning deployment—while providing practical, data-driven solutions for sustainable urban energy management.
