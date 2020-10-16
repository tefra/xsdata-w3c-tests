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
            "pattern": r"P\p{Nd}{1,4}Y\p{Nd}{1,2}MT\p{Nd}{1,2}H",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
