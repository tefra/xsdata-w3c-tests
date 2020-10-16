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
        :cvar VALUE_2001_03:
        :cvar VALUE_2000_10:
        :cvar VALUE_2001_12:
        """
        VALUE_2001_03 = "2001-03"
        VALUE_2000_10 = "2000-10"
        VALUE_2001_12 = "2001-12"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
