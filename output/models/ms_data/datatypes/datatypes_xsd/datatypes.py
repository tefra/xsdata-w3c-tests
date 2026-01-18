from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Data:
    class Meta:
        name = "data"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "item"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )
