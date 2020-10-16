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
        :cvar VALUE_03_15:
        :cvar VALUE_01_01:
        :cvar VALUE_10_01:
        """
        VALUE_03_15 = "--03-15"
        VALUE_01_01 = "--01-01"
        VALUE_10_01 = "--10-01"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
