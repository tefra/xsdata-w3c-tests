from dataclasses import dataclass, field
from typing import List


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: List[str] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
