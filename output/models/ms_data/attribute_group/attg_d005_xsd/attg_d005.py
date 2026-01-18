from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    att1: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    foo: None | int = field(
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
    bar: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_exclusive": 100,
        },
    )
    att3: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
