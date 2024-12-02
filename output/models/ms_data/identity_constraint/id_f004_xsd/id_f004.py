from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Uid:
    class Meta:
        name = "uid"

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    val2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    uid: list[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
