from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class FooTypeFoo(Enum):
    VALUE_MINUS_456 = -456
    VALUE_MINUS_789 = -789
    VALUE_0 = 0


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[FooTypeFoo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
