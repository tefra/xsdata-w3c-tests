from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    a_a: None | int = field(
        default=None,
        metadata={
            "name": "Aƻa",
            "type": "Attribute",
        },
    )
    b_b: None | int = field(
        default=None,
        metadata={
            "name": "bƻB",
            "type": "Attribute",
        },
    )
