import os
import json
from google import genai
from google.genai import types
from pydantic import BaseModel


class TreatmentPlan(BaseModel):
    summary: str
    goals: list[str]
    interventions: list[str]
    progress_tracking: str


client = genai.Client(api_key='AIzaSyBNqBv1vOHhU5bmg-05aMVJXrvXfLdqLb0')


def generate_treatment_plan(assessment_data):
    """Generate a treatment plan using Google's Gemini AI"""

    prompt = f"""
    As a mental health professional specializing in academic stress and student counseling, generate a comprehensive treatment plan based on the following assessment:

    Patient Information:
    - Name: {assessment_data['patient_info']['name']}
    - Age: {assessment_data['patient_info']['age']}
    - Gender: {assessment_data['patient_info']['gender']}
    - Primary Complaint: {assessment_data['patient_info']['primary_complaint']}
    - Duration: {assessment_data['patient_info']['duration']}

    Assessment Scores (0-10 scale):
    {json.dumps(assessment_data['assessment_scores'], indent=2)}

    Consider the following aspects specifically for students:
    1. Academic pressure and examination stress
    2. Study-life balance
    3. Time management
    4. Performance anxiety
    5. Parent and peer expectations

    Provide a treatment plan in JSON format with this structure:
    {{
        "summary": "Brief summary focusing on academic stress management",
        "goals": ["3-5 treatment goals including academic improvement"],
        "interventions": ["5-7 specific interventions for stress management"],
        "progress_tracking": "Description of progress tracking methods"
    }}

    Return only valid JSON, no additional text.
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type='application/json',
                response_schema=TreatmentPlan,
            ),
        )
        print(response.text)

        # Parse the response into JSON
        treatment_plan = json.loads(response.text)
        return treatment_plan
    except Exception as e:
        print(e)
        return {
            "summary": "Error generating treatment plan. Please try again.",
            "goals": ["Error occurred"],
            "interventions": ["Error occurred"],
            "progress_tracking": "Error occurred"
        }
