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
        :cvar VALUE_1985_04_12_T10_30_00:
        """
        VALUE_1985_04_12_T10_30_00 = "1985-04-12T10:30:00"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
