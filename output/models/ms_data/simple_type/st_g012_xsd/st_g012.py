from dataclasses import dataclass, field
from typing import List


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "required": True,
            "pattern": r"[A-C]{0,2}",
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
            "required": True,
            "pattern": r"[A-C]{0,2}",
            "tokens": True,
        }
    )
