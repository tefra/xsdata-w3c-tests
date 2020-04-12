import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--savexml",
        action="store_true",
        default=False,
        help="Save xsdata serialized documents.",
    )


@pytest.fixture
def save_xml(request):
    return request.config.getoption("--savexml")
