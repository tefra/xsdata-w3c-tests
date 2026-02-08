from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    value: int | bool | str = field(default="")
    idref_attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Wrapper:
    class Meta:
        name = "wrapper"

    root: Root = field(
        metadata={
            "type": "Element",
        }
    )
