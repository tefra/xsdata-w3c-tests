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
        VALUE_1999_05_31 = "1999-05-31"
        VALUE_1999_07_31 = "1999-07-31"
        VALUE_2000_03_10 = "2000-03-10"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
