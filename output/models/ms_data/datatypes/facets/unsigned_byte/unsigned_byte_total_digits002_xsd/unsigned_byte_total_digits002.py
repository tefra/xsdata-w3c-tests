from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "total_digits": 3,
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
