import streamlit as st
import json
from datetime import datetime
from utils import validate_input, create_assessment_questions
from ai_service import generate_treatment_plan
from data_handler import save_patient_data, load_patient_data

st.set_page_config(page_title="Mental Health Treatment Plan Generator",
                   page_icon="🧠",
                   layout="wide")


def main():
    st.title("🧠 Mental Health Treatment Plan Generator 🧠")

    st.warning("""
    **Medical Disclaimer**: This is an educational tool only. All treatment plans generated should be reviewed by a licensed mental health professional. 
    This tool does not provide medical advice or replace professional mental healthcare services.
    """)

    # Main input form
    st.header("Patient Information")

    with st.form("patient_info"):
        col1, col2 = st.columns(2)

        with col1:
            patient_name = st.text_input("Patient Name", key="name")
            age = st.number_input("Age", min_value=0, max_value=120, key="age")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"],
                                  key="gender")

        with col2:
            primary_complaint = st.text_area("Primary Complaint",
                                             key="complaint")
            duration = st.text_input("Duration of Symptoms", key="duration")

        st.subheader("Mental Health Assessment")

        # Assessment questions
        questions = create_assessment_questions()
        responses = {}

        for q_id, question in questions.items():
            responses[q_id] = st.slider(question,
                                        min_value=0,
                                        max_value=10,
                                        value=5,
                                        help="0 = Not at all, 10 = Severely")

        submitted = st.form_submit_button("Generate Treatment Plan")

    if submitted:
        if validate_input(patient_name, age, primary_complaint):
            with st.spinner("Generating treatment plan..."):
                # Prepare data for AI analysis
                assessment_data = {
                    "patient_info": {
                        "name": patient_name,
                        "age": age,
                        "gender": gender,
                        "primary_complaint": primary_complaint,
                        "duration": duration
                    },
                    "assessment_scores": responses
                }

                # Generate treatment plan
                treatment_plan = generate_treatment_plan(assessment_data)

                # Display treatment plan
                st.header("Generated Treatment Plan")

                # Save data
                save_data = {
                    "timestamp": datetime.now().isoformat(),
                    "assessment_data": assessment_data,
                    "treatment_plan": treatment_plan
                }
                saved_file = save_patient_data(patient_name, save_data)
                if saved_file:
                    st.success(f"Treatment plan saved successfully to {saved_file}")
                else:
                    st.error("Failed to save treatment plan")

                # Display sections
                st.subheader("Summary")
                st.write(treatment_plan["summary"])

                st.subheader("Treatment Goals")
                for goal in treatment_plan["goals"]:
                    st.markdown(f"- {goal}")

                st.subheader("Recommended Interventions")
                for intervention in treatment_plan["interventions"]:
                    st.markdown(f"- {intervention}")

                st.subheader("Progress Tracking")
                st.write(treatment_plan["progress_tracking"])

                # Download button for treatment plan
                st.download_button(
                    label="Download Treatment Plan",
                    data=json.dumps(treatment_plan, indent=2),
                    file_name=
                    f"treatment_plan_{patient_name}_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json")
        else:
            st.error(
                "Please fill in all required fields (Name, Age, Primary Complaint)"
            )


if __name__ == "__main__":
    main()
