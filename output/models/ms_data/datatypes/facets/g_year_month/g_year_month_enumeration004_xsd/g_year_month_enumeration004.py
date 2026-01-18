from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod


class FooTypeFoo(Enum):
    VALUE_2001_03 = XmlPeriod("2001-03")
    VALUE_2000_10 = XmlPeriod("2000-10")
    VALUE_2001_12 = XmlPeriod("2001-12")


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
