from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Data:
    class Meta:
        name = "data"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
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
