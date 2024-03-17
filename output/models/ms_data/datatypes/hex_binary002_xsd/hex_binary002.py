from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: List[bytes] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "tokens": True,
            "format": "base16",
        },
    )


@dataclass
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: List[bytes] = field(
        default_factory=list,
        metadata={
            "tokens": True,
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
    simple_test: Optional[SimpleTest] = field(
        default=None,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
        },
    )
