from dataclasses import dataclass, field
from typing import List


@dataclass
class Foo:
    class Meta:
        name = "foo"

    value: List[str] = field(
        default_factory=list,
        metadata={
            "pattern": r"[A-C]{0,2}",
            "tokens": True,
        },
    )
