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
        :cvar VALUE_1_1:
        :cvar VALUE_2_718:
        :cvar VALUE_3_14:
        """
        VALUE_1_1 = "1.1"
        VALUE_2_718 = "2.718"
        VALUE_3_14 = "3.14"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
