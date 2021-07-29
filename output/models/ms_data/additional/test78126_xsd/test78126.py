from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class A:
    class Meta:
        name = "a"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    att1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Any:
    class Meta:
        name = "any"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    any_or_a: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "any",
                    "type": Any,
                },
                {
                    "name": "a",
                    "type": A,
                },
            ),
        }
    )
