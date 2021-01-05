from dataclasses import dataclass, field
from enum import Enum
from typing import Optional
from xsdata.models.datatype import XmlDate


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
        VALUE_1999_05_31 = XmlDate(1999, 5, 31)
        VALUE_1999_07_31 = XmlDate(1999, 7, 31)
        VALUE_2000_03_10 = XmlDate(2000, 3, 10)


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
