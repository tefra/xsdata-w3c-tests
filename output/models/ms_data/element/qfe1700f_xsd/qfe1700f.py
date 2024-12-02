from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Uid:
    class Meta:
        name = "uid"
        nillable = True

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
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
            "nillable": True,
        },
    )
