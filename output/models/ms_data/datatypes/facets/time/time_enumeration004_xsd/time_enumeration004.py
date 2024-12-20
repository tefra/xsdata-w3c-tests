from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlTime


class FooTypeFoo(Enum):
    VALUE_13_20_00_05_00 = XmlTime(13, 20, 0, 0, -300)
    VALUE_13_20_00 = XmlTime(13, 20, 0, 0)
    VALUE_01_50_40 = XmlTime(1, 50, 40, 0)


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
