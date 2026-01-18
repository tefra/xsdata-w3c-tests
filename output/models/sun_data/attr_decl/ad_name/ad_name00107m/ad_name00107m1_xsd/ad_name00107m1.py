from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    number00: None | int = field(
        default=None,
        metadata={
            "name": "number00一",
            "type": "Attribute",
        },
    )
    number10: None | int = field(
        default=None,
        metadata={
            "name": "number10盒",
            "type": "Attribute",
        },
    )
    number20: None | int = field(
        default=None,
        metadata={
            "name": "number20龥",
            "type": "Attribute",
        },
    )
    number01: None | int = field(
        default=None,
        metadata={
            "name": "number01〇",
            "type": "Attribute",
        },
    )
    number02: None | int = field(
        default=None,
        metadata={
            "name": "number02〡",
            "type": "Attribute",
        },
    )
    number12: None | int = field(
        default=None,
        metadata={
            "name": "number12〥",
            "type": "Attribute",
        },
    )
    number22: None | int = field(
        default=None,
        metadata={
            "name": "number22〩",
            "type": "Attribute",
        },
    )
