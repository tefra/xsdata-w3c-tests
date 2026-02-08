from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "min_inclusive": Decimal("1.1"),
            "max_exclusive": Decimal("7.7"),
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
