import json
import os
from datetime import datetime


def save_patient_data(patient_name, data):
    """Save patient data to JSON file"""
    try:
        # Create a filename using patient name and timestamp
        filename = f"patient_{patient_name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json"

        # Save to file
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return filename
    except Exception as e:
        print(f"Error saving patient data: {e}")
        return None


def load_patient_data(patient_identifier):
    """Load patient data from JSON file"""
    try:
        if patient_identifier == "sample":
            return {
                "name": "John Doe",
                "age": 30,
                "gender": "Male",
                "complaint": "Experiencing anxiety and depression",
                "duration": "6 months"
            }

        filename = f"patient_{patient_identifier.lower().replace(' ', '_')}.json"
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return None
    except Exception as e:
        print(f"Error loading patient data: {e}")
        return None
