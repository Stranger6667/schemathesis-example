import schemathesis

schema = schemathesis.from_uri("http://0.0.0.0:8080/api/openapi.json")


@schema.parametrize(method="GET", endpoint="/bookings/{booking_id}")
def test_get_booking(case):
    response = case.call()
    assert response.status_code < 500
