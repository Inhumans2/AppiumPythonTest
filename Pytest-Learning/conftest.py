import pytest


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_make_report(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
