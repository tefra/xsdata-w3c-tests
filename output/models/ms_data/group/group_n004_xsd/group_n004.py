from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Elem:
    class Meta:
        name = "elem"

    a1: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem: Elem = field(
        metadata={
            "type": "Element",
        }
    )
