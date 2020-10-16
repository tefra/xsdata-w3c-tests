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
            "min_exclusive": "10:21:00-05:00",
            "max_inclusive": "13:20:00-04:00",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
