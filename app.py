import streamlit as st
import pandas as pd

st.title("⚡ Advanced EV vs. Petrol TCO Simulator")
st.write("A deep-dive Total Cost of Ownership model accounting for inflation, insurance, and battery degradation.")

# --- SIDEBAR: BASIC INPUTS ---
st.sidebar.header("1. Commute Profile")
daily_km = st.sidebar.slider("Daily Commute (km)", 10, 200, 50)
years = st.sidebar.slider("Years of Ownership", 5, 15, 12)

# --- SIDEBAR: ADVANCED ECONOMICS ---
st.sidebar.header("2. Economic Parameters")
petrol_inflation = st.sidebar.slider("Annual Petrol Inflation (%)", 0.0, 10.0, 5.0)
elec_inflation = st.sidebar.slider("Annual Electricity Inflation (%)", 0.0, 10.0, 3.0)

battery_replace_year = st.sidebar.slider("Battery Replacement Year", 5, 12, 8)
battery_replace_cost = st.sidebar.number_input("Battery Replacement Cost (₹)", value=450000, step=50000)

# Constants (Baseline: Petrol vs EV Compact SUV)
petrol_car_cost = 1000000  # ₹10 Lakhs On-Road
ev_car_cost = 1450000      # ₹14.5 Lakhs On-Road

petrol_price_base = 100.0  # ₹/Litre
elec_rate_base = 7.0       # ₹/kWh

petrol_mileage = 15.0      # km/l
ev_efficiency = 0.12       # kWh/km

# Annual Fixed Costs
petrol_maint = 12000
ev_maint = 6000
petrol_insurance = 25000
ev_insurance = 35000

# --- SIMULATION ENGINE ---
annual_km = daily_km * 365
data = []

cum_petrol = petrol_car_cost
cum_ev = ev_car_cost

for year in range(1, years + 1):
    # 1. Apply Compound Inflation
    curr_petrol_price = petrol_price_base * ((1 + petrol_inflation/100) ** (year - 1))
    curr_elec_rate = elec_rate_base * ((1 + elec_inflation/100) ** (year - 1))
    
    # 2. Calculate Annual Running Costs
    petrol_running = (annual_km / petrol_mileage) * curr_petrol_price
    ev_running = (annual_km * ev_efficiency) * curr_elec_rate
    
    # 3. Add Fixed Annual Costs
    petrol_total_yr = petrol_running + petrol_maint + petrol_insurance
    ev_total_yr = ev_running + ev_maint + ev_insurance
    
    # 4. Inject the Battery Replacement Edge Case
    if year == battery_replace_year:
        ev_total_yr += battery_replace_cost
        
    # 5. Accumulate
    cum_petrol += petrol_total_yr
    cum_ev += ev_total_yr
    
    data.append({
        "Year": year,
        "Petrol Car (₹)": int(cum_petrol),
        "Electric Vehicle (₹)": int(cum_ev)
    })

# --- VISUALIZATION ---
df = pd.DataFrame(data).set_index("Year")
st.subheader("Cumulative Cost Trajectory")
st.line_chart(df)

# Final Output Logic
diff = int(cum_petrol - cum_ev)
if diff > 0:
    st.success(f"**Result:** The EV saves you ₹{diff:,} over {years} years.")
else:
    st.error(f"**Result:** The Petrol car saves you ₹{-diff:,} over {years} years.")