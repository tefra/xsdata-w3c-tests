from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[object] = field(default=None)


@dataclass
class Item:
    class Meta:
        name = "item"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    a_or_item: list[Union[A, Item]] = field(
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
