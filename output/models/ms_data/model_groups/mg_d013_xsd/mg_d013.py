from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elt1:
    class Meta:
        name = "elt1"

    elt2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elt3: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    elt4: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    elt1: list[Elt1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
