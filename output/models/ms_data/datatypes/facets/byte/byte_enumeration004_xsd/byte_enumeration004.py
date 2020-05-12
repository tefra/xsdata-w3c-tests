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
        :cvar VALUE_MINUS_1:
        :cvar VALUE_0:
        :cvar VALUE_1:
        """
        VALUE_MINUS_1 = -1
        VALUE_0 = 0
        VALUE_1 = 1


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
