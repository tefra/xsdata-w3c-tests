from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
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
        """
        :cvar VALUE_1985_04_12_T10_30_00:
        :cvar VALUE_1985_04_12_T12_00_00:
        :cvar VALUE_1999_07_31_T01_00_00:
        """
        VALUE_1985_04_12_T10_30_00 = "1985-04-12T10:30:00"
        VALUE_1985_04_12_T12_00_00 = "1985-04-12T12:00:00"
        VALUE_1999_07_31_T01_00_00 = "1999-07-31T01:00:00"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
