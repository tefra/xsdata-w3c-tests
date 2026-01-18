from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    id1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    id2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    multiple_ids: Ids = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
