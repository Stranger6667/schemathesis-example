import pytest
import schemathesis
from hypothesis import settings, given

schema = schemathesis.from_uri(
    "http://127.0.0.1:5000/api/openapi.json"
)


@pytest.fixture
def token():
    return "spam"


@schema.parametrize(
    operation_id="app.views.create_booking"
)
# @settings(max_examples=1000)
def test_app(case, token):
    assert case.body["id"] > 10000
    case.headers = {"Authorization": f"Bearer {token}"}
    response = case.call()
    case.validate_response(response)


@given(
    create=schema["/bookings/"]["POST"].as_strategy(),
    get=schema["/bookings/{booking_id}"]["GET"].as_strategy(),
)
def test_stateful(create, get):
    response = create.call()
    create.validate_response(response)
    if response.status_code == 201:
        get.path_parameters["booking_id"] = response.json()["id"]
        response = get.call()
        get.validate_response(response)
