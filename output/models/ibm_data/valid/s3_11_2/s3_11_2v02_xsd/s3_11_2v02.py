from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class Numtype:
    class Meta:
        name = "numtype"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    id_1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id_2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    number: list[Numtype] = field(
        default_factory=list,
        metadata={
            "name": "Number",
            "type": "Element",
            "min_occurs": 1,
        },
    )
