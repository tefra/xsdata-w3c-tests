# xsdata-w3c-tests

[![Build Status](https://github.com/tefra/xsdata-w3c-tests/workflows/tests/badge.svg)](https://github.com/tefra/xsdata-w3c-tests/actions)

Run xsdata code generator and data binding modules against the W3C XML Schema 1.1 test
suite.

The invalid schema tests are ignored (~12k tests) as xsdata is not really a validator.

# XSD Mode

Each test case will generate the models for the schema document, parse the xml instance
document and serialize it back to xml checking that the output is still valid.

```terminal
$ pytest -n 4  --mode xsd --runxfail --save-output
```

Results: **5** failed, **14580** passed, **89** skipped, **16** warnings

The save output option will store the output xml document. The xml mode's drawback is
that it doesn't do any quality checks that all elements and values actually match the
original document.
