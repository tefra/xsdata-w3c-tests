from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    str00_a: None | str = field(
        default=None,
        metadata={
            "name": "str00Aー",
            "type": "Attribute",
        },
    )
    str10: None | str = field(
        default=None,
        metadata={
            "name": "str10-ヽ",
            "type": "Attribute",
        },
    )
    str20: None | str = field(
        default=None,
        metadata={
            "name": "str20ヾ",
            "type": "Attribute",
        },
    )
