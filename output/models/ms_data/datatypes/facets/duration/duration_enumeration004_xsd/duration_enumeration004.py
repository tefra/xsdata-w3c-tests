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
        P1347_Y = "P1347Y"
        P1347_M = "P1347M"
        P1_Y2_MT2_H = "P1Y2MT2H"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
