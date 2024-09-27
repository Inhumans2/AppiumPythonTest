import pytest


def test_validate_titles():
    expected_value = "Google.com"
    actual_value = "Gmail.com"
    title = "I have Gmail account"

    print("Beginning")
    assert expected_value == actual_value, "Values are not matching"
    assert "Gmails" in title, "Value not present in the title"
    assert False, "forcefully failing the case"
    print("Ending")
