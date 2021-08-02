from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "tokens": True,
        }
    )


@dataclass
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
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
    simple_test: List[str] = field(
        default_factory=list,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "required": True,
            "tokens": True,
        }
    )
