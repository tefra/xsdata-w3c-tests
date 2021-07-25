from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Uid:
    class Meta:
        name = "uid"
        nillable = True

    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    uid: List[Uid] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
            "nillable": True,
        }
    )
