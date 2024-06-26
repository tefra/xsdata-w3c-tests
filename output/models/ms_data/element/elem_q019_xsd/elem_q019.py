from dataclasses import dataclass, field
from typing import Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(init=False, default="Hello")


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: Optional[FooTest] = field(
        default=None,
        metadata={
            "name": "fooTest",
            "type": "Element",
        },
    )
