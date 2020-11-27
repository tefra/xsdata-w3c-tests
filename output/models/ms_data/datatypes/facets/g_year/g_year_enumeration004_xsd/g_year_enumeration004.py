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
        VALUE_2000 = "2000"
        VALUE_1999 = "1999"
        VALUE_2038 = "2038"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
