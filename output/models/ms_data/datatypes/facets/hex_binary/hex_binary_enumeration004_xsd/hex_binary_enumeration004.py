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
        :cvar ABCEDF:
        :cvar ADF789:
        :cvar VALUE_0123456789:
        """
        ABCEDF = "abcedf"
        ADF789 = "adf789"
        VALUE_0123456789 = "0123456789"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
