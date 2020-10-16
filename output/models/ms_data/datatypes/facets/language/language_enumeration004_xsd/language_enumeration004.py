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
        :cvar EN:
        :cvar FR:
        :cvar DE:
        """
        EN = "en"
        FR = "fr"
        DE = "de"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
