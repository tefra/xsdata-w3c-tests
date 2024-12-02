from dataclasses import dataclass, field
from typing import Optional

from output.models.ms_data.identity_constraint.id_f029_xsd.id_f029a import R


@dataclass
class T:
    class Meta:
        name = "t"

    r: Optional[R] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "importNS",
            "required": True,
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

    t: list[T] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
