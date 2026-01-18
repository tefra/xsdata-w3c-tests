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
    att2: str = field(
        init=False,
        default="bar",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass(kw_only=True)
class BE1(BCt):
    class Meta:
        name = "b-e1"
        namespace = "ns-a"
