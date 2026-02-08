from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlPeriod


class FooTypeFoo(Enum):
    VALUE_2000 = XmlPeriod("2000")
    VALUE_1999 = XmlPeriod("1999")
    VALUE_2038 = XmlPeriod("2038")


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
