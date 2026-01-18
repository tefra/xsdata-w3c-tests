from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Chap:
    class Meta:
        name = "chap"

    de: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    fr: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    en: None | object = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    chap: list[Chap] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    lang: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
