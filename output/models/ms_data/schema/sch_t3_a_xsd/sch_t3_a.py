from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "ns-a"


@dataclass(kw_only=True)
class ACt:
    class Meta:
        name = "A-ct"

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
        }
    )
    att9: object = field(
        metadata={
            "type": "Attribute",
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
class E2:
    class Meta:
        name = "e2"
        namespace = "ns-a"

    value: int = field(
        metadata={
            "total_digits": 2,
        }
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "ns-a"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class E1(ACt):
    class Meta:
        name = "e1"
        namespace = "ns-a"
