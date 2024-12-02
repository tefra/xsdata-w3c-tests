from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "length": 2,
            "tokens": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        },
    )
