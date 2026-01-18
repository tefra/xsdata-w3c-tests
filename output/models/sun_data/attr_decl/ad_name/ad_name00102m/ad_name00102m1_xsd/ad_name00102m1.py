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
            "name": "一00",
            "type": "Attribute",
        },
    )
    value_01: None | int = field(
        default=None,
        metadata={
            "name": "盒01",
            "type": "Attribute",
        },
    )
    value_02: None | int = field(
        default=None,
        metadata={
            "name": "龥02",
            "type": "Attribute",
        },
    )
    value_10: None | int = field(
        default=None,
        metadata={
            "name": "〇10",
            "type": "Attribute",
        },
    )
    value_20: None | int = field(
        default=None,
        metadata={
            "name": "〡20",
            "type": "Attribute",
        },
    )
    value_21: None | int = field(
        default=None,
        metadata={
            "name": "〥21",
            "type": "Attribute",
        },
    )
    value_22: None | int = field(
        default=None,
        metadata={
            "name": "〩22",
            "type": "Attribute",
        },
    )
