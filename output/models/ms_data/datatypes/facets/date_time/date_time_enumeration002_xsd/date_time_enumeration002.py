from dataclasses import dataclass, field
from datetime import datetime
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
        VALUE_1985_04_12_T10_30_00 = datetime(1985, 4, 12, 10, 30)


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
