from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    value_00: None | int = field(
        default=None,
        metadata={
            "name": "_00",
            "type": "Attribute",
        },
    )
