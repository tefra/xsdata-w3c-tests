from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    class Foo(Enum):
        VALUE_1_1 = Decimal("1.1")
        VALUE_3_14 = Decimal("3.14")
        VALUE_2_718 = Decimal("2.718")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
