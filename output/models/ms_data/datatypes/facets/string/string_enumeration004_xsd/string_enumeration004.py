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
        :cvar FOO:
        :cvar FOO123:
        """
        VALUE_123 = "123"
        FOO = "foo"
        FOO123 = "foo123"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
