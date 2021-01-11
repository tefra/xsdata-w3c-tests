from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDateTime


class FooTypeFoo(Enum):
    VALUE_1985_04_12_T10_30_00 = XmlDateTime(1985, 4, 12, 10, 30, 0)
    VALUE_1985_04_12_T12_00_00 = XmlDateTime(1985, 4, 12, 12, 0, 0)
    VALUE_1999_07_31_T01_00_00 = XmlDateTime(1999, 7, 31, 1, 0, 0)


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
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
