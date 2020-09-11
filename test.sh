#!/usr/bin/env sh

SCHEMA_URL="http://0.0.0.0:8080/api/openapi.json"

# Zero config
schemathesis run $SCHEMA_URL

# Select what to test
schemathesis run -E booking -M POST $SCHEMA_URL

# What checks to run
schemathesis run -c status_code_conformance $SCHEMA_URL

# Include your own checks
schemathesis --pre-run hooks run $SCHEMA_URL

# Provide auth & headers
schemathesis run -H "Authorization: Bearer <token>" $SCHEMA_URL

# Configure hypothesis parameters
schemathesis run --hypothesis-max-examples 1000 $SCHEMA_URL

# Run in multiple threads
schemathesis run -w 8 $SCHEMA_URL

# Store network log
schemathesis run --store-network-log=cassette.yaml $SCHEMA_URL
# Replay existing
schemathesis replay cassette.yaml

# Stateful testing
schemathesis run --stateful=links $SCHEMA_URL
