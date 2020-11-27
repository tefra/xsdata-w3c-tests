from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional


@dataclass
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: List[Decimal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )


@dataclass
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: Optional[Decimal] = field(
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

    complex_test: List[ComplexTest] = field(
        default_factory=list,
        metadata={
            "name": "complexTest",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    simple_test: List[Decimal] = field(
        default_factory=list,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "min_occurs": 1,
        }
    )
