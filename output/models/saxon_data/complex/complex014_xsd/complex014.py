from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True

    e: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    f: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
