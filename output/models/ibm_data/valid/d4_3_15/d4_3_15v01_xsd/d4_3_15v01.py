from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class RootType:
    class Meta:
        name = "rootType"

    ele: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    min: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    max: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root(RootType):
    class Meta:
        name = "root"
