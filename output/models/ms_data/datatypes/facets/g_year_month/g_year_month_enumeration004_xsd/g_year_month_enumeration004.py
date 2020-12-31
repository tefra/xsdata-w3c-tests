from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import Period


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional["FooType.Foo"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    class Foo(Enum):
        VALUE_2001_03 = Period("2001-03")
        VALUE_2000_10 = Period("2000-10")
        VALUE_2001_12 = Period("2001-12")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
