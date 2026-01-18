from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(kw_only=True)
class MyType:
    class Meta:
        name = "myType"

    value: Decimal = field(
        metadata={
            "required": True,
        }
    )


@dataclass(kw_only=True)
class FooType(MyType):
    class Meta:
        name = "fooType"


@dataclass(kw_only=True)
class Root(FooType):
    class Meta:
        name = "root"
