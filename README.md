# Advanced EV vs. Petrol TCO Simulator (EnergyVerse ⚡)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://advancedevpetroltcosimulator-md7gj3txjvdjsdohwqvaug.streamlit.app/)

## Overview
This application is an interactive Total Cost of Ownership (TCO) simulator built with Python and Streamlit. It is designed to help users accurately compare the long-term financial impact of owning an Electric Vehicle (EV) versus a traditional Petrol car[cite: 1]. Instead of just calculating basic fuel savings, the engine models real-world economic variables including compound inflation, yearly maintenance, insurance premiums, and the major edge-case cost of EV battery replacement[cite: 1].

---

## Key Features[cite: 1]
* **Interactive Commute Profiling:** Users can adjust their expected daily commute distances and total years of ownership to match their personal lifestyle[cite: 1].
* **Dynamic Economic Parameters:** Simulates the compounding impact of annual inflation rates for both petrol and electricity over the ownership period[cite: 1].
* **Battery Replacement Logic:** Explicitly factors in the year and cost of replacing an EV battery, preventing skewed data and providing a realistic long-term cost trajectory[cite: 1].
* **Visual Cost Trajectory:** Automatically generates a line chart using Pandas and Streamlit to illustrate the cumulative cost comparison year-by-year[cite: 1].
* **Clear Financial Verdict:** Calculates the final total costs and displays a bold bottom-line result, showing exactly how much money is saved and which vehicle type is the better financial choice[cite: 1].

---

## Dependencies[cite: 1]
To run this application, you must have Python installed along with the following libraries[cite: 1]:
* `streamlit`[cite: 1]
* `pandas`[cite: 1]

---
