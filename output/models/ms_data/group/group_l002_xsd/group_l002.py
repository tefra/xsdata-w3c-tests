from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Elem:
    class Meta:
        name = "elem"

    b1_or_b2: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "b1",
                    "type": object,
                    "namespace": "",
                },
                {
                    "name": "b2",
                    "type": object,
                    "namespace": "",
                },
            ),
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    elem: Optional[Elem] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
