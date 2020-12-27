from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Union


@dataclass
class Outer:
    class Meta:
        name = "outer"

    value: List[Union[str, datetime]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
class Value:
    class Meta:
        name = "value"

    value: Optional[Union[str, datetime]] = field(
        default=None,
    )
