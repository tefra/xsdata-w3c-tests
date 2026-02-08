from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime


class FooTypeFoo(Enum):
    VALUE_1985_04_12_T10_30_00 = XmlDateTime(1985, 4, 12, 10, 30, 0)


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
