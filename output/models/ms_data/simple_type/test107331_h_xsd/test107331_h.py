from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    class Meta:
        name = "a"

    value: Optional[object] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Item:
    class Meta:
        name = "item"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "required": True,
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    item: List[Item] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
