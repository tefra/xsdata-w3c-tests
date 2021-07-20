from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    uid: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Uid:
    class Meta:
        name = "uid"

    value: Optional[str] = field(
        default=None
    )
