import streamlit as st
from team_a_triage import run_triage_module
from team_b_drugs import run_drug_module

st.set_page_config(page_title="Integrated CDSS Platform", page_icon="🏥", layout="centered")

st.warning("⚠️ **Disclaimer:** This is a demo, not a medical diagnosis.")

st.title("🏥 Integrated Clinical Decision Support System")
st.write("End-to-end clinical workflow integrating **Sub-Team A (Patient Triage)** and **Sub-Team B (Prescription Safety)**.")

with st.sidebar:
    st.header("👥 Team Structure (8 Members)")
    st.markdown("**Sub-Team A (Triage Module):**\n- Members 1–4 (`team_a_triage.py`)")
    st.markdown("**Sub-Team B (Drug Checker):**\n- Members 5–8 (`team_b_drugs.py`)")
    st.divider()
    st.caption("Data flows automatically from Module 1 to Module 2 via Streamlit Session State.")

tab1, tab2 = st.tabs(["🩺 Step 1: Patient Triage (Team A)", "💊 Step 2: Drug Checker (Team B)"])

with tab1:
    run_triage_module()

with tab2:
    run_drug_module()

with st.expander("Limitations, Bias, and Clinical Ethics (Human-in-the-Loop)"):
    st.write(
        "- **Human-in-the-Loop:** Assists clinicians with rule-based alerts; doctors retain final decision authority.\n"
        "- **Rule-Table Scope:** Covers 6 common medications and 4 vital thresholds; unlisted reactions require full hospital databases.\n"
        "- **Alert Fatigue:** Over-triggering warnings in real hospitals can desensitize doctors to critical alerts.\n"
        "- **Privacy:** Runs in-memory with zero patient data stored or logged."
    )
