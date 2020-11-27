from dataclasses import dataclass, field
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
        VALUE_MINUS_1 = -1
        VALUE_0 = 0
        VALUE_1 = 1


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
