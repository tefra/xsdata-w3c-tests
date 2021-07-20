from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Uid:
    class Meta:
        name = "uid"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
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
        }
    )
