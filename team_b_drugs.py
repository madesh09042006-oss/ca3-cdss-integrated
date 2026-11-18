import streamlit as st

def run_drug_module():
    st.subheader("Module 2: Drug-Interaction Alert Checker (Sub-Team B)")
    st.caption("Developed by Sub-Team B | Rule-Based Prescription Safety")

    triage_level = st.session_state.get("triage_level", "Not Evaluated Yet")
    patient_age = st.session_state.get("patient_age", None)

    st.info(f"📋 **Synced Patient Status from Module 1:** {triage_level}" + (f" (Age: {patient_age})" if patient_age else ""))

    medicines = [
        "Aspirin (Pain / Blood Thinner)",
        "Warfarin (Anticoagulant)",
        "Ibuprofen (NSAID Painkiller)",
        "Amoxicillin (Antibiotic)",
        "Metformin (Diabetes)",
        "Atorvastatin (Cholesterol)"
    ]

    col1, col2 = st.columns(2)
    with col1:
        med1 = st.selectbox("Current Medicine", medicines, index=0)
    with col2:
        med2 = st.selectbox("New Prescription", medicines, index=1)

    interactions = {
        frozenset(["Aspirin (Pain / Blood Thinner)", "Warfarin (Anticoagulant)"]): (
            "HIGH RISK",
            "Increases risk of severe internal bleeding due to combined blood-thinning effects."
        ),
        frozenset(["Aspirin (Pain / Blood Thinner)", "Ibuprofen (NSAID Painkiller)"]): (
            "MODERATE RISK",
            "Combining two NSAIDs raises stomach ulcer risk and lowers Aspirin's heart-protective effect."
        ),
        frozenset(["Warfarin (Anticoagulant)", "Ibuprofen (NSAID Painkiller)"]): (
            "HIGH RISK",
            "Ibuprofen irritates gastric lining and amplifies Warfarin anticoagulation."
        ),
        frozenset(["Metformin (Diabetes)", "Atorvastatin (Cholesterol)"]): (
            "SAFE / LOW RISK",
            "Standard combination for diabetic care; routine monitoring recommended."
        ),
    }

    if st.button("Check Drug Interaction"):
        if med1 == med2:
            st.warning("Select two different medicines to run an interaction check.")
        else:
            pair = frozenset([med1, med2])
            if pair in interactions:
                severity, reason = interactions[pair]
                if "HIGH" in severity:
                    st.error(f"🛑 **{severity} INTERACTION:** {reason}")
                elif "MODERATE" in severity:
                    st.warning(f"⚠️ **{severity} INTERACTION:** {reason}")
                else:
                    st.success(f"✅ **{severity}:** {reason}")
            else:
                st.info("ℹ️ **No Major Interaction Found** in our demo rule table. Verify with a pharmacist.")

            if patient_age and patient_age >= 65 and ("Ibuprofen (NSAID Painkiller)" in pair or "Warfarin (Anticoagulant)" in pair):
                st.warning("👵 **Integrated Age Alert (from Module 1):** Patient is 65+, increasing sensitivity to NSAID/anticoagulant side effects.")
