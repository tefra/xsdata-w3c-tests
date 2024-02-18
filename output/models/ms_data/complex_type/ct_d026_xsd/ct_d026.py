from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional


@dataclass
class MyType:
    class Meta:
        name = "myType"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
