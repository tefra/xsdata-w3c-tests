from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Para:
    class Meta:
        name = "para"

    value: str = field(default="")
    id_one: None | str = field(
        default=None,
        metadata={
            "name": "id-one",
            "type": "Attribute",
        },
    )
    id_two: None | str = field(
        default=None,
        metadata={
            "name": "id-two",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
