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
        :cvar P1347_M:
        :cvar P1347_Y:
        :cvar P1_Y2_MT2_H:
        """
        P1347_M = "P1347M"
        P1347_Y = "P1347Y"
        P1_Y2_MT2_H = "P1Y2MT2H"


@dataclass
class Test(FooType):
    class Meta:
        name = "test"