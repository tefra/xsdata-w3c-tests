from enum import Enum
from dataclasses import dataclass, field
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
        :cvar VALUE_123:
        :cvar VALUE_456:
        :cvar VALUE_789:
        """
        VALUE_123 = 123
        VALUE_456 = 456
        VALUE_789 = 789


@dataclass
class Test(FooType):
    class Meta:
        name = "test"