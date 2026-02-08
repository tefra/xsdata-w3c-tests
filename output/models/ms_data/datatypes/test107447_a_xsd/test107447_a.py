from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    token: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    language: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    name: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    ncname: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    id: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    idref: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    idrefs: list[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
    nmtoken: str = field(
        init=False,
        default=" John    ",
        metadata={
            "type": "Element",
        },
    )
    nmtokens: list[str] = field(
        init=False,
        default_factory=lambda: [
            "John",
        ],
        metadata={
            "type": "Element",
            "tokens": True,
        },
    )
