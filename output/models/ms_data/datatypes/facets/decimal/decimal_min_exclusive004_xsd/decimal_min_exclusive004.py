from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": Decimal("1.1"),
            "max_inclusive": Decimal("7.7"),
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
