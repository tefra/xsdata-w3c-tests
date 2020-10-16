from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    """
    :ivar foo:
    """
    class Meta:
        name = "fooType"

    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "max_inclusive": 1,
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
