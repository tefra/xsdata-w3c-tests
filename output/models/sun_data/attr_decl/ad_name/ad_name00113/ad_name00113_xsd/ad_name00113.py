from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "AttrDecl/name"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "AttrDecl/name"

    aa111a2_aa: None | int = field(
        default=None,
        metadata={
            "name": "aa111a2Aa",
            "type": "Attribute",
        },
    )
    aa22_b3c: None | int = field(
        default=None,
        metadata={
            "name": "aa22B3c",
            "type": "Attribute",
        },
    )
    aa3_4: None | int = field(
        default=None,
        metadata={
            "name": "aa3-4_",
            "type": "Attribute",
        },
    )
