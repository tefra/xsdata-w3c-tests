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
        :cvar VALUE_2000:
        """
        VALUE_2000 = "2000"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
