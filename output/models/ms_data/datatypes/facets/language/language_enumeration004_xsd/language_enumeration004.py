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
        :cvar DE:
        :cvar EN:
        :cvar FR:
        """
        DE = "de"
        EN = "en"
        FR = "fr"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"