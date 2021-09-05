import pytest
import json


@pytest.fixture
def invoice():
    return {
        "date": "2021-09-05 12:13:14",
    }


@pytest.fixture
def invoice_item():
    return {
        "units": 1,
        "description": "This is a short test description",
        "ammount": 19.50,
    }


class TestApi:
    pass
