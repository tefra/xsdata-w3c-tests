from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Root:
    total1: Optional[int] = field(
        default=None,
        metadata={
            "name": "Total1",
            "type": "Element",
            "namespace": "",
            "total_digits": 3,
        }
    )
    total2: Optional[int] = field(
        default=None,
        metadata={
            "name": "Total2",
            "type": "Element",
            "namespace": "",
            "min_exclusive": 100,
            "total_digits": 3,
        }
    )
