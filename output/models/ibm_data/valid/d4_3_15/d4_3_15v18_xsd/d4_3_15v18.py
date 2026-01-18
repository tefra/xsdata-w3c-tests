from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    value: None | object = field(default=None)
    attr: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
