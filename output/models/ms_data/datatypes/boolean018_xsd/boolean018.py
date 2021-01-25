from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class ComplexfooTypeCompFoo(Enum):
    VALUE_0 = False
    VALUE_1 = True


class SimplefooType(Enum):
    TRUE_VALUE = True
    FALSE_VALUE = False


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: Optional[ComplexfooTypeCompFoo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: Optional[SimplefooType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


@dataclass
class Root:
    class Meta:
        name = "root"

    complex_test: Optional[ComplexTest] = field(
        default=None,
        metadata={
            "name": "complexTest",
            "type": "Element",
            "required": True,
        }
    )
    simple_test: Optional[SimplefooType] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
        }
    )
