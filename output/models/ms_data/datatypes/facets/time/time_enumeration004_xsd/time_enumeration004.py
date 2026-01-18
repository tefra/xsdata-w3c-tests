from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlTime


class FooTypeFoo(Enum):
    VALUE_13_20_00_05_00 = XmlTime(13, 20, 0, 0, -300)
    VALUE_13_20_00 = XmlTime(13, 20, 0, 0)
    VALUE_01_50_40 = XmlTime(1, 50, 40, 0)


@dataclass(kw_only=True)
class FooType:
    class Meta:
        name = "fooType"

    foo: FooTypeFoo = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Test(FooType):
    class Meta:
        name = "test"
