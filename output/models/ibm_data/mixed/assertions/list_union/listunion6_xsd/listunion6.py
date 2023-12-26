from dataclasses import dataclass, field
from typing import List


@dataclass
class ListType:
    class Meta:
        name = "list"

    value: List[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
