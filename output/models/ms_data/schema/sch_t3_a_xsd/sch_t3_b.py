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
    att2: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att3: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att5: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att6: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att7: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att9: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att11: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "total_digits": 1,
        }
    )
    att12: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )
    att13: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        }
    )
    att14: str = field(
        default="abc",
        metadata={
            "type": "Attribute",
        }
    )
    att15: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        }
    )
    att16: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
