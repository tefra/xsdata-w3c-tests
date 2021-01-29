# xsdata-w3c-tests

[![Build Status](https://github.com/tefra/xsdata-w3c-tests/workflows/tests/badge.svg)](https://github.com/tefra/xsdata-w3c-tests/actions)

Run xsdata code generator and data binding modules against the W3C XML Schema 1.1 test
suite.

The invalid schema tests are ignored (~12k tests) as xsdata is not really a validator.

# XML Mode

Each test case will generate the models for the schema document, parse the xml instance
document and serialize it back to xml checking that the output is still valid.

```terminal
$ pytest -n 4 --runxfail --save-output
```

Results: **10** failed, **14577** passed, **88** skipped, **18** warnings

The save output option will store the output xml document. The xml mode's drawback is
that it doesn't do any quality checks that all elements and values actually match the
original document.

# JSON Mode

Each test case will generate the models for the schema document, parse the xml instance
document and serialize it to json, parse the json document and compare the initial
python object to the object after the roundtrip conversion.

```terminal
$ pytest -n 4 --json-360 --runxfail --save-output
```

Results: **114** failed, **14561** passed, **25** warnings

Most of the failures involve test cases with complex instances with wildcards and
derived types.
