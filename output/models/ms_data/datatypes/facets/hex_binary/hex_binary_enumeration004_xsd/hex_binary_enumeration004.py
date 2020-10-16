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
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )

    class Foo(Enum):
        """
        :cvar ADF789:
        :cvar ABCEDF:
        :cvar VALUE_0123456789:
        """
        ADF789 = "adf789"
        ABCEDF = "abcedf"
        VALUE_0123456789 = "0123456789"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
