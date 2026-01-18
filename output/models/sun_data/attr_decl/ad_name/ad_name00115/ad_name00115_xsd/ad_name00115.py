from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    low_line_hyphen_minus_full_stop: None | int = field(
        default=None,
        metadata={
            "name": "_-.",
            "type": "Attribute",
        },
    )
    value_0: None | int = field(
        default=None,
        metadata={
            "name": "_-0.",
            "type": "Attribute",
        },
    )
