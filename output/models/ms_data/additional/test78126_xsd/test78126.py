from dataclasses import dataclass, field
from typing import List, Optional, Union


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
class AnyType:
    class Meta:
        name = "any"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    any_or_a: List[Union[A, AnyType]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "any",
                    "type": AnyType,
                },
                {
                    "name": "a",
                    "type": A,
                },
            ),
        }
    )
