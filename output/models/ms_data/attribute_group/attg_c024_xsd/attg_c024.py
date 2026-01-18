from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class B:
    e: None | object = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )


@dataclass(kw_only=True)
class Abc(B):
    class Meta:
        name = "abc"

    att: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att2: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc(Abc):
    class Meta:
        name = "doc"
