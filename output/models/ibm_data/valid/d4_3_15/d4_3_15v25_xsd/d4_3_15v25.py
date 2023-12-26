from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"

    e1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
