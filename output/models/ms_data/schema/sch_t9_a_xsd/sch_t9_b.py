from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "ns-a"


@dataclass
class BCt:
    class Meta:
        name = "b-ct"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: str = field(
        default="bar",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
