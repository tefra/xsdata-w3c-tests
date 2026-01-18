from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ids:
    class Meta:
        name = "ids"

    id1: str = field(
        init=False,
        default="zxc",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    a: Ids = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
