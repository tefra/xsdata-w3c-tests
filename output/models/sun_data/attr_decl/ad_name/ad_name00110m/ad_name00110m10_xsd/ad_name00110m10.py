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
            "name": "str00A⃐",
            "type": "Attribute",
        },
    )
    str10: None | str = field(
        default=None,
        metadata={
            "name": "str10-⃖",
            "type": "Attribute",
        },
    )
    str20: None | str = field(
        default=None,
        metadata={
            "name": "str20⃜",
            "type": "Attribute",
        },
    )
    str01_a: None | str = field(
        default=None,
        metadata={
            "name": "str01A⃡",
            "type": "Attribute",
        },
    )
    str02_a: None | str = field(
        default=None,
        metadata={
            "name": "str02A〪",
            "type": "Attribute",
        },
    )
    str12: None | str = field(
        default=None,
        metadata={
            "name": "str12-〬",
            "type": "Attribute",
        },
    )
    str22: None | str = field(
        default=None,
        metadata={
            "name": "str22〯",
            "type": "Attribute",
        },
    )
    str03_a: None | str = field(
        default=None,
        metadata={
            "name": "str03A゙",
            "type": "Attribute",
        },
    )
    str04_a: None | str = field(
        default=None,
        metadata={
            "name": "str04A゚",
            "type": "Attribute",
        },
    )
