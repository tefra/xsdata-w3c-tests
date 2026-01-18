from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDate


class FooTypeFoo(Enum):
    VALUE_1999_05_31 = XmlDate(1999, 5, 31)
    VALUE_1999_07_31 = XmlDate(1999, 7, 31)
    VALUE_2000_03_10 = XmlDate(2000, 3, 10)


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
