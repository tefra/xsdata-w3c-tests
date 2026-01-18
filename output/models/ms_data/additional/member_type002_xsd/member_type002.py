from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Ct:
    class Meta:
        name = "ct"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    att: None | bool | int | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    e: list[Ct] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
