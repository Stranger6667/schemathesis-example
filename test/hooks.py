from datetime import timedelta

import schemathesis
from hypothesis import strategies as st


@st.composite
def fullname(draw):
    first = draw(st.sampled_from(["jonh", "jane"]))
    last = draw(st.just("doe"))
    return f"{first} {last}"


schemathesis.register_string_format("fullname", fullname())


@schemathesis.hooks.register
def before_generate_body(context, strategy):
    return strategy.filter(lambda x: x["id"] > 10000)


@schemathesis.register_check
def not_so_slow(response, case):
    assert response.elapsed < timedelta(milliseconds=100), "Response is slow!"


@schemathesis.register_target
def big_response(context):
    return float(len(context.response.content))
