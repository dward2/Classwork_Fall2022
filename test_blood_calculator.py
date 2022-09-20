import pytest


@pytest.mark.parametrize("HDL_input, expected",
                         [(85, "Normal"),
                          (45, "Borderline Low"),
                          (20, "Low")])
def test_check_HDL_Normal(HDL_input, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_input)
    assert answer == expected


@pytest.mark.parametrize("LDL_input, expected",
                         [(125, "Normal"),
                          (130, "Borderline high"),
                          (165, "High"),
                          (190, "Very high")])
def test_check_LDL(LDL_input, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_input)
    assert answer == expected


@pytest.mark.parametrize("total_input, expected",
                         [(190, "Normal"),
                          (230, "Borderline high"),
                          (240, "High")])
def test_check_total_cholesterol(total_input, expected):
    from blood_calculator import check_total_cholesterol
    answer = check_total_cholesterol(total_input)
    assert answer == expected
