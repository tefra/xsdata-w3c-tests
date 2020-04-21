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
        :cvar VALUE_1999:
        :cvar VALUE_2000:
        :cvar VALUE_2038:
        """
        VALUE_1999 = "1999"
        VALUE_2000 = "2000"
        VALUE_2038 = "2038"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
