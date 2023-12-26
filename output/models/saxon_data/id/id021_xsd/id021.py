from dataclasses import dataclass, field
from typing import List


@dataclass
class Para:
    class Meta:
        name = "para"

    e: str = field(
        default="entity1 entity2",
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: List[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
