from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar value:
    """
    class Meta:
        name = "fooType"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class MyType:
    """
    :ivar value:
    """
    class Meta:
        name = "myType"

    value: Optional[str] = field(
        default=None,
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
