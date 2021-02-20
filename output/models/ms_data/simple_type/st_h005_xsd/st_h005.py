from dataclasses import dataclass, field
from typing import List


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[0-8]{5}",
            "tokens": True,
        }
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
            "pattern": r"[0-8]{5}",
            "tokens": True,
        }
    )
