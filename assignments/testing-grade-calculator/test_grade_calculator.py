from grade_calculator import calculate_letter_grade


def test_score_in_a_range_returns_a():
    assert calculate_letter_grade(95) == "A"