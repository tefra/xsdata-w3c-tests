# xsdata-w3c-tests

[![Build Status](https://travis-ci.org/tefra/xsdata-w3c-tests.svg?branch=master)](https://travis-ci.org/tefra/xsdata-w3c-tests)

Run xsdata code generator and data binding module against the W3C XML Schema 1.1 test
suite.

# Report

1078 failed, 25099 passed, 147 skipped, 12 warnings

# Methodology

- Invalid schema tests cases are skipped.
- Generate dataclasses for given schema.
  - **Fail** when cli raises exception or expected module::class is not found.
- Parse the given xml instance.
  - **Fail** when parser raises exception and xml instance is valid.
- Serialize to xml and validate against the schema.
  - **Fail** if xml instance is valid and final output is invalid.

# Test runner info

- Generate tests instead of using pytest parametrizing.
- Use pytest cache to generate the xfail decorators for ci.
- Cache code generation runs.
- Cache xml validator instances.
- Output directory remains after each build.

```terminal
pip install -r requirements.txt
python generate.py  # Run twice to add the xfail decorators from pytest cache
```
