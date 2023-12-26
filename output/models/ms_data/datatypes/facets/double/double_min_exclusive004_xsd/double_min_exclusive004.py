from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_exclusive": 1.1,
            "max_inclusive": 7.7,
        },
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
