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
        :cvar VALUE_13_20_00_05_00:
        """
        VALUE_13_20_00_05_00 = "13:20:00-05:00"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
