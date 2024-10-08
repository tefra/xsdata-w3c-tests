from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Doc:
    class Meta:
        name = "doc"

    foo: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_length": 6,
        },
    )
    att: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_length": 6,
        },
    )
