from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class A:
    class Meta:
        name = "a"

    value: None | object = field(default=None)


@dataclass(kw_only=True)
class Item:
    class Meta:
        name = "item"

    any_element: None | object = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    a_or_item: list[A | Item] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "a",
                    "type": A,
                },
                {
                    "name": "item",
                    "type": Item,
                },
            ),
        },
    )
