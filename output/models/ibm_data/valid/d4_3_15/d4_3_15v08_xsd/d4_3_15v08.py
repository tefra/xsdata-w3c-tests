from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ComType:
    class Meta:
        name = "comType"

    value: int = field(
        metadata={
            "required": True,
        }
    )
    attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(ComType):
    class Meta:
        name = "root"
