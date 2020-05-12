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
        :cvar VALUE_567:
        :cvar VALUE_1:
        :cvar VALUE_234:
        """
        VALUE_567 = 567
        VALUE_1 = 1
        VALUE_234 = 234


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
