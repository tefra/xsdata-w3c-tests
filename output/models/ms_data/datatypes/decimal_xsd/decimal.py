from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: Decimal = field()


@dataclass(kw_only=True)
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    complex_test: ComplexTest = field(
        metadata={
            "name": "complexTest",
            "type": "Element",
        }
    )
    simple_test: SimpleTest = field(
        metadata={
            "name": "simpleTest",
            "type": "Element",
        }
    )
