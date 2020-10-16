from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": "P1Y1MT1H",
            "max_inclusive": "P2Y3MT2H",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
