import pytest


@pytest.fixture()
def convert_string(request):
    orig = request.param
    converted = request.param.replace("_", " ").title()
    yield {"orig": orig, "converted": converted}
