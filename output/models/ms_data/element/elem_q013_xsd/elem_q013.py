from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: Optional[str] = field(
        default=None
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
        }
    )
