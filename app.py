import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Scholar Bio-Sync", page_icon="🎓")

st.title("🎓 Scholar Bio-Sync: Performance Predictor")
st.write("### Optimize your 9.28 SGPI potential today.")

# --- Data Scientist Input Sidebar ---
st.sidebar.header("Daily Data Entry")
sleep_hours = st.sidebar.slider("Hours of Sleep", 0.0, 10.0, 6.0)
commute_time = st.sidebar.slider("Commute Exhaustion (1-10)", 1, 10, 5)
assignment_load = st.sidebar.number_input("Assignments Pending", 0, 10, 2)

# --- The "Brain": Mock Predictive Model ---
# In a real app, you'd train this on your own historical data!
def predict_performance(s, c, a):
    # Logic: More sleep = good, more commute/work = bad
    base_score = 70
    score = base_score + (s * 5) - (c * 3) - (a * 4)
    return min(max(score, 0), 100)

if st.button("CALCULATE MY PEAK FOCUS"):
    focus_result = predict_performance(sleep_hours, commute_time, assignment_load)
    
    st.divider()
    st.subheader(f"Your Focus Score: {focus_result}%")
    st.progress(focus_result / 100)
    
    if focus_result > 80:
        st.success("🔥 Peak Performance! High chance of retaining complex Deep Learning concepts.")
    elif focus_result > 50:
        st.info("⚡ Moderate Focus. Stick to Python scripting or cleaning datasets.")
    else:
        st.warning("😴 High Burnout Risk. Put the laptop down and rest for the Kalyan commute tomorrow.")

    # Data Scientist Visualization
    chart_data = pd.DataFrame({
        "Factor": ["Sleep", "Commute", "Assignments"],
        "Impact": [sleep_hours * 5, -commute_time * 3, -assignment_load * 4]
    })
    st.bar_chart(chart_data, x="Factor", y="Impact")

st.markdown("---")
st.caption("Built for Data Scientists who juggle internships, academics, and early mornings.")
