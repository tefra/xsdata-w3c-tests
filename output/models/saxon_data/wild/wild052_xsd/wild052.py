from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Zang:
    class Meta:
        name = "zang"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class Zing:
    class Meta:
        name = "zing"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "process_contents": "skip",
        }
    )
