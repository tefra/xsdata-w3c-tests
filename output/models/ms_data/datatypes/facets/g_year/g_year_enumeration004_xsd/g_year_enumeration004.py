from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlPeriod


class FooTypeFoo(Enum):
    VALUE_2000 = XmlPeriod("2000")
    VALUE_1999 = XmlPeriod("1999")
    VALUE_2038 = XmlPeriod("2038")


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
