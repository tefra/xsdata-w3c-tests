from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Bad:
    class Meta:
        name = "bad"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Good:
    class Meta:
        name = "good"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )


@dataclass
class Perfect:
    class Meta:
        name = "perfect"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
