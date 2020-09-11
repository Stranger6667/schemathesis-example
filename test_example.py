import hypothesis
import schemathesis
from hypothesis import given, strategies as st

# Useful hypothesis profile for CI testing
hypothesis.settings.register_profile("CI", max_examples=10000)

# The main entrypoint
schema = schemathesis.from_uri("http://0.0.0.0:8080/api/openapi.json")


@schema.parametrize(
    method="GET",
    endpoint="/bookings/{booking_id}",
    # tag="booking",
    # operation_id="booking.get",
)
# Set hypothesis config
# @settings(max_examples=1000, phases=[Phase.explicit])
def test_get_booking(case: schemathesis.Case):
    # Set parameters manually
    case.path_parameters["user_id"] = 42
    # Make a network call
    response = case.call()
    # Assert the result
    assert response.status_code < 500
    # Or run built-in assertions
    case.validate_response(response)

# TODO. WSGI example


# These are usual hypothesis strategies
@given(
    get=schema["/bookings/{booking_id}"]["GET"].as_strategy(),
    post=schema["/bookings/"]["POST"].as_strategy(),
)
def test_with_strategy(get, post):
    pass


# Adjust data generation
@schemathesis.hooks.register
def before_generate_query(context, strategy):
    return strategy.filter(lambda x: x["id"].isdigit())


# Custom string formats
def card_number():
    # Use Luhn algorithm here
    return st.just("4444111100001111")


schemathesis.register_string_format("card_number", card_number())

# TODO. database reset example