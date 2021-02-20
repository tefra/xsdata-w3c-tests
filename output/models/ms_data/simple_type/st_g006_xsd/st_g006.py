from dataclasses import dataclass, field
from typing import List


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "length": 2,
            "tokens": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: List[int] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "length": 2,
            "tokens": True,
        }
    )
