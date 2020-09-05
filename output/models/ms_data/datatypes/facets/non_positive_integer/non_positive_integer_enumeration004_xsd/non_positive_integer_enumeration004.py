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
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )

    class Foo(Enum):
        """
        :cvar VALUE_MINUS_456:
        :cvar VALUE_MINUS_789:
        :cvar VALUE_0:
        """
        VALUE_MINUS_456 = -456
        VALUE_MINUS_789 = -789
        VALUE_0 = 0


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
