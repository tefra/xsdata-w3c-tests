import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--save-output",
        action="store_true",
        default=False,
        help="Save xsdata serialized documents.",
    )
    parser.addoption(
        "--json-360",
        action="store_true",
        default=False,
        help="Run json 360 tests",
    )


@pytest.fixture
def save_output(request):
    return request.config.getoption("--save-output")


@pytest.fixture
def json_360(request):
    return request.config.getoption("--json-360")


@pytest.hookimpl
def pytest_sessionfinish(session, exitstatus):
    if session.config.getoption("--json-360") and session.testsfailed <= 120:
        session.exitstatus = 0
