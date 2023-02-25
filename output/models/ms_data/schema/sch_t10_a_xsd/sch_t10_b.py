from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    class Meta:
        name = "b-ct"

    att1: Optional[object] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: str = field(
        init=False,
        default="bar",
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
