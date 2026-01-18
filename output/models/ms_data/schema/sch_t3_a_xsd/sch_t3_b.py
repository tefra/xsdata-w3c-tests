from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class BCt:
    class Meta:
        name = "b-ct"

    att1: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att3: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att5: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att6: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att7: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att9: object = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    att11: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "total_digits": 1,
        },
    )
    att12: object = field(
        default="abc",
        metadata={
            "type": "Attribute",
        },
    )
    att13: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        },
    )
    att14: object = field(
        default="abc",
        metadata={
            "type": "Attribute",
        },
    )
    att15: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        },
    )
    att16: str = field(
        init=False,
        default="fix",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
