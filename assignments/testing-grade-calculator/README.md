# 📘 Assignment: Testing a Grade Calculator

## 🎯 Objective

Write automated tests for a grade calculator using pytest. Practice organizing test cases, checking boundary values, and verifying that invalid input raises the correct exception.

## 📝 Tasks

### 🛠️	Test Common Scores

#### Description
Review `grade_calculator.py` and the example in `test_grade_calculator.py`. Add tests for scores that clearly fall within each remaining letter-grade range, then run them with `pytest`.

#### Requirements
Completed program should:

- Include at least one test for each letter grade from A through F
- Use descriptive test function names that explain the behavior being checked
- Pass all tests when you run `pytest`


### 🛠️	Test Grade Boundaries

#### Description
Test the exact score where each letter grade begins and a score immediately below it. Use `pytest.mark.parametrize` to keep these related cases concise.

#### Requirements
Completed program should:

- Test the boundaries at 90, 80, 70, and 60
- Test one score immediately below each boundary
- Use one parametrized test for the boundary cases


### 🛠️	Test Invalid Scores

#### Description
Verify that the calculator rejects values outside the allowed range. Use `pytest.raises` to check the expected exception.

#### Requirements
Completed program should:

- Verify that a score below 0 raises `ValueError`
- Verify that a score above 100 raises `ValueError`
- Leave the complete test suite passing