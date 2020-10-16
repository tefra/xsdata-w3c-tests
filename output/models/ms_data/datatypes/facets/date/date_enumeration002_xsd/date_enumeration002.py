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
        :cvar VALUE_1999_05_31:
        """
        VALUE_1999_05_31 = "1999-05-31"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
