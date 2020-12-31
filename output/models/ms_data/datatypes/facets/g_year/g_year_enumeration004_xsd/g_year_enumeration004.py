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
        VALUE_2000 = Period("2000")
        VALUE_1999 = Period("1999")
        VALUE_2038 = Period("2038")


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
