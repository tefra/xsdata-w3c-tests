from dataclasses import dataclass, field
from typing import Optional


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
class FooType(MyType):
    class Meta:
        name = "fooType"



@dataclass
class Root(FooType):
    class Meta:
        name = "root"
