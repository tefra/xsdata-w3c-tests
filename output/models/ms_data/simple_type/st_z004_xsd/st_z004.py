from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Element1:
    class Meta:
        name = "element1"

    attribute1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(あ|ｱ)*",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    element1: list[Element1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
