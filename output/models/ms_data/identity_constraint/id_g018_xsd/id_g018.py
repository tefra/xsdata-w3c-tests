from dataclasses import dataclass, field
from typing import List, Optional

from output.models.ms_data.identity_constraint.id_g018_xsd.id_g018a import R


@dataclass
class T:
    class Meta:
        name = "t"

    r: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "importNS",
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    t: List[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
