from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

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
    att3: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att4: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    att5: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc(Test):
    class Meta:
        name = "doc"
