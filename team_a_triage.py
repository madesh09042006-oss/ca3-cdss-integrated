import streamlit as st

def run_triage_module():
    st.subheader("Module 1: Patient Risk & Triage Engine (Sub-Team A)")
    st.caption("Developed by Sub-Team A | Clinical Vitals & Priority Scoring")

    col1, col2 = st.columns(2)
    with col1:
        age = st.slider("Patient Age", 1, 100, 52)
        systolic_bp = st.slider("Systolic BP (mmHg)", 80, 220, 130)
    with col2:
        temp_f = st.slider("Body Temperature (°F)", 96.0, 105.0, 98.6, step=0.1)
        chest_pain = st.checkbox("Chest Pain / Shortness of Breath")

    if st.button("Run Triage Assessment"):
        score = 0
        flags = []

        if chest_pain:
            score += 3
            flags.append("Acute chest/breathing symptom")
        if systolic_bp >= 160 or systolic_bp <= 90:
            score += 2
            flags.append(f"Abnormal BP ({systolic_bp} mmHg)")
        if temp_f >= 102.0:
            score += 2
            flags.append(f"High fever ({temp_f} °F)")
        if age >= 65:
            score += 1
            flags.append("Senior age factor (65+)")

        if score >= 3:
            level = "HIGH PRIORITY"
            st.error(f"🚨 **{level}** (Score: {score}/8) — Immediate physician review needed.")
        elif score >= 1:
            level = "MODERATE PRIORITY"
            st.warning(f"⚠️ **{level}** (Score: {score}/8) — Prompt consultation advised.")
        else:
            level = "LOW PRIORITY"
            st.success(f"✅ **{level}** (Score: {score}/8) — Stable vitals.")

        if flags:
            st.write("**Triggered Clinical Rules:** " + " | ".join(flags))

        st.session_state["triage_level"] = level
        st.session_state["patient_age"] = age
        st.info("🔗 Triage status synced to **Module 2 (Drug-Alert Checker)**.")
