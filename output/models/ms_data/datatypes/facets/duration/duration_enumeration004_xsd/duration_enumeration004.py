from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDuration


class FooTypeFoo(Enum):
    P1347_Y = XmlDuration("P1347Y")
    P1347_M = XmlDuration("P1347M")
    P1_Y2_MT2_H = XmlDuration("P1Y2MT2H")


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
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
