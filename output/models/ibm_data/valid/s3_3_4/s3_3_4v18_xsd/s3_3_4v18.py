from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    union_of_ids: None | int | bool | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    idref: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
