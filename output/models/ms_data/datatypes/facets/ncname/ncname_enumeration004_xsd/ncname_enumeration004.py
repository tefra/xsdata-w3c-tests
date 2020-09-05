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
        :cvar FOO:
        :cvar FOO123:
        :cvar FU1:
        """
        FOO = "foo"
        FOO123 = "foo123"
        FU1 = "fu1"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
