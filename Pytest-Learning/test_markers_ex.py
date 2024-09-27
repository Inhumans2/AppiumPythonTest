import pytest


def get_data():
    return [
        ("agarwalanirudh88@gmail.com", "fekjwhefbjk"),
        ("anirudha@hike.in", "sefbhjbhjfew"),
        ("radhag97@gmail.com", "jknecdjbde")
    ]


@pytest.mark.functional
def test_login():
    print("Login Flow")


@pytest.mark.regression
def test_user_reg():
    print("User Registration flow")


@pytest.mark.functional
def test_forgot_password():
    print("Forgot Password Flow")


@pytest.mark.skip
def test_case_skip():
    print("Skipping the case")


@pytest.mark.parametrize("username,password", get_data())
def test_login_kero(username, password):
    print(username, "-----", password)