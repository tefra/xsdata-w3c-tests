from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Duration


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
        P1347_Y = Duration("P1347Y")
        P1347_M = Duration("P1347M")
        P1_Y2_MT2_H = Duration("P1Y2MT2H")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"