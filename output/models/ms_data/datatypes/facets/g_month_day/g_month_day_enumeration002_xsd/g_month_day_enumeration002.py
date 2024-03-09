from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlPeriod


class FooTypeFoo(Enum):
    VALUE_03_15 = XmlPeriod("--03-15")


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
