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
        :cvar VALUE_15:
        :cvar VALUE_01:
        :cvar VALUE_30:
        """
        VALUE_15 = "---15"
        VALUE_01 = "---01"
        VALUE_30 = "---30"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
