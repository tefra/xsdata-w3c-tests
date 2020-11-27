from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
            "min_inclusive": "10:21:00-05:00",
            "max_exclusive": "13:20:00-04:00",
        }
    )


@dataclass
class Test(FooType):
    class Meta:
        name = "test"
