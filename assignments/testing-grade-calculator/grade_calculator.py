def calculate_letter_grade(score: float) -> str:
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"