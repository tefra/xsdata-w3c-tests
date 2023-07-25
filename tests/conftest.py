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
        choices=["xsd", "build"],
        help="Mode",
    )
    parser.addoption(
        "--output-format",
        action="store",
        default="dataclasses",
        choices=["dataclasses", "attrs", "pydantic"],
        help="Mode",
    )


@pytest.fixture
def save_output(request):
    return request.config.getoption("--save-output")


@pytest.fixture
def mode(request):
    return request.config.getoption("--mode")


@pytest.fixture
def output_format(request):
    return request.config.getoption("--output-format")
