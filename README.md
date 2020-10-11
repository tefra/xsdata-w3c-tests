# xsdata-w3c-tests

[![Build Status](https://github.com/tefra/xsdata-w3c-tests/workflows/tests/badge.svg)](https://github.com/tefra/xsdata-w3c-tests/actions)

Run xsdata code generator and data binding module against the W3C XML Schema 1.1 test
suite.

# Report

13 failed, 14574 passed, 88 skipped, 38 warnings

# Methodology

- Invalid schema tests or no schema tests are ignored (~12k tests)
- Generate dataclasses for given schema.
  - **Fail** when cli raises exception or expected module::class is not found.
- Parse the given xml instance.
  - **Fail** when parser raises exception.
- Serialize to xml and validate against the schema.
  - **Fail** if final output is invalid.
  - **Skip** if original instance or schema also fail validation.

# Test runner info

- Generate tests instead of using pytest parametrizing.
- Use pytest cache to generate the xfail decorators for ci.
- Cache code generation runs.
- Cache validator instances.
- Output directory remains after each build.

```terminal
pip install -r requirements.txt
pytest -n 4 --tb short tests/
pytest -n 4 --runxfail --tb short tests/  | tee pytest.log  # to run the known failing tests
python generate.py  # update xfail markers
```
