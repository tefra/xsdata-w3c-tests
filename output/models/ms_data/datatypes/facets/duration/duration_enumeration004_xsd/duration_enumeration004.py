from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDuration


class FooTypeFoo(Enum):
    P1347_Y = XmlDuration("P1347Y")
    P1347_M = XmlDuration("P1347M")
    P1_Y2_MT2_H = XmlDuration("P1Y2MT2H")


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooTypeFoo = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
