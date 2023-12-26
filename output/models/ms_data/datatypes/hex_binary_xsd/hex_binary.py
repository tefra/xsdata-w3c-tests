from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: Optional[bytes] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "format": "base16",
        },
    )


@dataclass
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base16",
        },
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
        },
    )
    simple_test: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
            "format": "base16",
        },
    )
