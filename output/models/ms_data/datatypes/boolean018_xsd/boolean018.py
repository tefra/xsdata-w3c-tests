from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class ComplexfooTypeCompFoo(Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"


class SimplefooType(Enum):
    TRUE = True
    FALSE = False


@dataclass(kw_only=True)
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: ComplexfooTypeCompFoo = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: SimplefooType = field(
        metadata={
            "required": True,
        }
    )


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
            "required": True,
        }
    )
    simple_test: SimpleTest = field(
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
        }
    )
