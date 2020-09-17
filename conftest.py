from hypothesis import settings
from hooks import *


settings.register_profile("CI", max_examples=1000)
