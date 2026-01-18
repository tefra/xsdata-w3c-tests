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
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
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
