import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Scholar Bio-Sync", page_icon="🎓", layout="centered")

# Custom CSS for the "Scholar" aesthetic
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Scholar Bio-Sync")
st.write("### Predictive Performance & Burnout Tracker")
st.info("Optimize your 9.28 SGPI potential by balancing rest and commute fatigue.")

# --- Sidebar Inputs ---
st.sidebar.header("📊 Daily Biometrics")
sleep_hours = st.sidebar.slider("Sleep Duration (Hours)", 0.0, 12.0, 6.5)
commute_stress = st.sidebar.slider("Commute Fatigue (Kalyan-Nerul)", 1, 10, 5)
academic_load = st.sidebar.number_input("Pending Assignments/ML Tasks", 0, 20, 3)

# --- Predictive Logic (Data Science Weighted Calculation) ---
def predict_focus(sleep, commute, load):
    # Base focus starts at 50%
    # Positive weights: Sleep
    # Negative weights: Commute, Load
    score = (sleep * 8) - (commute * 3.5) - (load * 2.5) + 25
    return int(np.clip(score, 0, 100))

if st.button("RUN PERFORMANCE ANALYSIS"):
    focus_score = predict_focus(sleep_hours, commute_stress, academic_load)
    
    # Metrics Display
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Focus Capacity", f"{focus_score}%")
    with col2:
        burnout_level = 100 - focus_score
        st.metric("Burnout Risk", f"{burnout_level}%", delta_color="inverse")

    st.divider()

    # Data Storytelling (Visuals)
    if focus_score > 80:
        st.success("🔥 **Peak Academic Mode:** Perfect for complex Data Science research or TIFR prep.")
        st.balloons()
    elif focus_score > 50:
        st.info("⚡ **Stable Focus:** Good for Power BI dashboards or Python debugging.")
    else:
        st.warning("😴 **Recovery Needed:** High burnout detected. Prioritize rest before the next 5:30 AM alarm.")

    # Impact Chart
    st.write("#### Cognitive Impact Breakdown")
    impact_data = pd.DataFrame({
        "Metric": ["Restoration", "Travel Drain", "Academic Stress"],
        "Impact Value": [sleep_hours * 8, -(commute_stress * 3.5), -(academic_load * 2.5)]
    })
    st.bar_chart(impact_data, x="Metric", y="Impact Value")

st.markdown("---")
st.caption("Designed for Data Science students balancing internships and academics. | 📍 Kalyan, MH")

