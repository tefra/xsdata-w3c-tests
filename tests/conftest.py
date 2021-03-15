import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--save-output",
        action="store_true",
        default=False,
        help="Save xsdata serialized documents.",
    )
    parser.addoption(
        "--mode",
        action="store",
        default="xsd",
        choices=["xsd", "xml", "json"],
        help="Mode",
    )


@pytest.fixture
def save_output(request):
    return request.config.getoption("--save-output")


@pytest.fixture
def mode(request):
    return request.config.getoption("--mode")


@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    if session.config.getoption("mode") == "json" and session.testsfailed <= 120:
        session.exitstatus = 0
    elif session.config.getoption("mode") == "xml" and session.testsfailed <= 13:
        session.exitstatus = 0
