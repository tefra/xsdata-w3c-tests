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
            "name": "number00_",
            "type": "Attribute",
        },
    )
    number01: None | int = field(
        default=None,
        metadata={
            "name": "number01.",
            "type": "Attribute",
        },
    )
    number02: None | int = field(
        default=None,
        metadata={
            "name": "number02-",
            "type": "Attribute",
        },
    )
