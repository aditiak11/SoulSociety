def validate_input(name, age, complaint):
    """Validate user input fields"""
    if not name or not age or not complaint:
        return False
    return True


def create_assessment_questions():
    """Create standardized assessment questions focused on academic stress"""
    return {
        "academic_stress":
        "How would you rate your current level of academic stress?",
        "exam_anxiety":
        "How severe is your examination anxiety?",
        "sleep":
        "How would you rate your sleep quality during exam preparation?",
        "concentration":
        "How would you rate your ability to concentrate during study sessions?",
        "physical_symptoms":
        "How severe are physical symptoms of stress (headaches, stomach aches, etc.)?",
        "study_routine":
        "How satisfied are you with your current study routine?",
        "support_system":
        "How would you rate your current support system (family/friends/teachers)?",
        "confidence":
        "How would you rate your confidence in exam preparation?",
        "time_management":
        "How would you rate your time management skills?",
        "coping_mechanisms":
        "How effective are your current stress coping mechanisms?"
    }
